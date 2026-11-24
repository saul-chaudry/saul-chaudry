# Saul Chaudry

Senior Software & Platform Engineer based in Philadelphia, PA. Focused on cloud-native infrastructure, distributed systems, Kubernetes platforms, and developer tooling across Go, Python, and TypeScript.

---

### What I Build

- **Platform Engineering & GitOps:** Automated multi-cluster workload delivery, blue-green deployment gates, and declarative reconciliation using Kubernetes, ArgoCD, and Terraform.
- **Reliability & Incident Operations:** Real-time SLO tracking, synthetic health probing, and automated drift detection comparing live cloud state to baseline infrastructure definitions.
- **Distributed Services & APIs:** High-throughput microservices, event-driven pipelines, and gRPC control planes with strict boundary validation and structured observability.

---

### Featured Projects

#### [deployment-control-plane](https://github.com/saul-chaudry/deployment-control-plane)
Multi-environment release orchestration control plane with automated pre-deployment verification gates, canary traffic shifting, and one-click rollback triggers.  
`TypeScript` `Node.js` `Kubernetes` `Docker` `GitHub Actions`

#### [kubernetes-operator](https://github.com/saul-chaudry/kubernetes-operator)
Custom Kubernetes controller built with the Operator SDK to automate stateful application lifecycles, health checks, backup triggers, and pod failover.  
`Go` `Operator SDK` `Kubernetes API` `Custom Resources`

#### [infrastructure-drift-detector](https://github.com/saul-chaudry/infrastructure-drift-detector)
Automated infrastructure audit engine that continuously scans AWS and Azure resources to detect and report configuration drift against declarative Terraform baselines.  
`Python` `Terraform` `AWS Boto3` `Azure SDK` `Policy-as-Code`

#### [incident-status-platform](https://github.com/saul-chaudry/incident-status-platform)
Distributed incident response coordinator providing multi-tenant status page updates, automated SLO burn-rate alerts, and on-call escalation workflows.  
`TypeScript` `React` `Node.js` `PostgreSQL` `WebSockets`

#### [multi-cloud-gitops-platform](https://github.com/saul-chaudry/multi-cloud-gitops-platform)
Declarative GitOps pipeline managing synchronized application state across AWS EKS and Azure AKS clusters with policy validation.  
`Go` `ArgoCD` `Kubernetes` `Helm` `AWS EKS` `Azure AKS`

#### [cloud-compliance-scanner](https://github.com/saul-chaudry/cloud-compliance-scanner)
Continuous security posture scanner evaluating IAM roles, network access controls, and storage encryption rules against CIS security benchmarks.  
`Python` `AWS IAM` `Security Posture` `CIS Benchmarks`

#### [kubernetes-microservices-platform](https://github.com/saul-chaudry/kubernetes-microservices-platform)
Service-mesh microservices topology featuring mutual TLS communication, distributed tracing with OpenTelemetry, and resilient circuit breaking.  
`Java` `Spring Boot` `Kubernetes` `OpenTelemetry` `Docker`

#### [aks-deployment-platform](https://github.com/saul-chaudry/aks-deployment-platform)
Enterprise deployment pipeline for Azure Kubernetes Service with automated namespace isolation, ingress routing, and health verification.  
`C#` `.NET` `Azure AKS` `Helm` `GitHub Actions`

---

### Core Stack & Tooling

```
Cloud & Platforms   ::  AWS, Azure, Kubernetes, Docker, Helm, ArgoCD, Terraform
Languages           ::  Go, Python, TypeScript, JavaScript, Java, C# / .NET, Bash
Data & Storage      ::  PostgreSQL, Redis, MySQL, S3, Azure Blob
Observability       ::  OpenTelemetry, Prometheus, Grafana, Datadog
Architecture        ::  Event-Driven Systems, GitOps, Microservices, REST & gRPC
```

---

### Engineering Principles

- **Declarative by Default:** If it lives in production, it is defined in version control, reconciled continuously, and deployed through an automated pipeline.
- **Fail Closed & Observable:** Systems should expose clear telemetry, fail predictably without corrupting state, and self-heal whenever possible.
- **Least Privilege:** Zero standing access for production environments; credentials are short-lived, audited, and strictly scoped.

---

<p align="center">
  <sub>Portfolio: <a href="https://saulchaudry-se.vercel.app">saulchaudry-se.vercel.app</a> · GitHub: <a href="https://github.com/saul-chaudry">github.com/saul-chaudry</a> · Location: Philadelphia, PA</sub>
</p>
