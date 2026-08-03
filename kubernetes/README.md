# Kubernetes Deployment

This directory contains Kubernetes manifests used to deploy the SecureBank application.

## Components

- Namespace
- MySQL Deployment
- MySQL Service
- SecureBank Deployment
- SecureBank Service
- ConfigMap
- Secret
- Multi-container Pod
- Init Container

## Deployment Order

```text
Namespace
      ↓
ConfigMap
      ↓
Secret
      ↓
MySQL
      ↓
SecureBank
      ↓
Service
```

## Verify

```bash
kubectl get all -n securebank
```
