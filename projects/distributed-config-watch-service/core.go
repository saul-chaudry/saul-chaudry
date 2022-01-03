package core

import (
	"crypto/sha256"
	"encoding/hex"
	"errors"
	"fmt"
	"sync"
)

type Record struct {
	ID       string
	TenantID string
	Version  int
	Payload  string
	Digest   string
}

type Engine struct {
	mu          sync.RWMutex
	records     map[string]Record
	idempotency map[string]string
}

func NewEngine() *Engine {
	return &Engine{
		records:     make(map[string]Record),
		idempotency: make(map[string]string),
	}
}

func (e *Engine) Apply(tenantID, id, idemKey, payload string) (Record, error) {
	if tenantID == "" || id == "" || idemKey == "" {
		return Record{}, errors.New("tenantID, id, and idemKey are required")
	}
	e.mu.Lock()
	defer e.mu.Unlock()

	scopedIdem := tenantID + ":" + idemKey
	if key, ok := e.idempotency[scopedIdem]; ok {
		return e.records[key], nil
	}

	scopedKey := tenantID + ":" + id
	ver := 1
	if prev, ok := e.records[scopedKey]; ok {
		ver = prev.Version + 1
	}
	sum := sha256.Sum256([]byte(fmt.Sprintf("%s:%s:%d:%s", tenantID, id, ver, payload)))
	rec := Record{
		ID:       id,
		TenantID: tenantID,
		Version:  ver,
		Payload:  payload,
		Digest:   hex.EncodeToString(sum[:]),
	}
	e.records[scopedKey] = rec
	e.idempotency[scopedIdem] = scopedKey
	return rec, nil
}

func (e *Engine) Get(tenantID, id string) (Record, bool) {
	e.mu.RLock()
	defer e.mu.RUnlock()
	r, ok := e.records[tenantID+":"+id]
	return r, ok
}
