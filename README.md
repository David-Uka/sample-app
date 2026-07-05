# sample-app

Minimal HTTP service used as the demo workload for
[`gitops-manifests`](https://github.com/David-Uka/gitops-manifests), deployed
by ArgoCD onto the cluster from
[`terraform-eks-cluster`](https://github.com/David-Uka/terraform-eks-cluster).

## Pipeline (`.github/workflows/ci.yml`)
On push to `main`:
1. Build the image.
2. Scan it with `anchore/scan-action` (fails on `high`+ severity).
3. Push to `ghcr.io/david-uka/sample-app` tagged `sha-<short>` and `dev`.
4. Clone `gitops-manifests`, `kustomize edit set image` in
   `apps/sample-app/overlays/dev`, commit, push. ArgoCD auto-syncs dev.

## Promotion (`.github/workflows/promote.yml`)
Manual `workflow_dispatch`: pick `staging` or `prod` + an image tag (usually a
`sha-<short>` that already passed dev). Bumps that overlay the same way.
Prod's ArgoCD Application has `prune: false`, so promotion is deliberate.
