---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Application Development"
themes: ["GitOps Delivery"]
speakers: ["Jesse Suen", "Akuity"]
sched_url: https://kccncna2025.sched.com/event/27Fdg/bringing-oci-into-the-gitops-world-jesse-suen-akuity
youtube_search_url: https://www.youtube.com/results?search_query=Bringing+OCI+Into+the+GitOps+World+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Bringing OCI Into the GitOps World - Jesse Suen, Akuity

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Application Development]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Atlanta
- Speakers: Jesse Suen, Akuity
- Schedule: https://kccncna2025.sched.com/event/27Fdg/bringing-oci-into-the-gitops-world-jesse-suen-akuity
- Busca YouTube: https://www.youtube.com/results?search_query=Bringing+OCI+Into+the+GitOps+World+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Bringing OCI Into the GitOps World.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fdg/bringing-oci-into-the-gitops-world-jesse-suen-akuity
- YouTube search: https://www.youtube.com/results?search_query=Bringing+OCI+Into+the+GitOps+World+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=eCIovuFwodk
- YouTube title: Bringing OCI Into the GitOps World - Jesse Suen, Akuity
- Match score: 0.871
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/bringing-oci-into-the-gitops-world/eCIovuFwodk.txt
- Transcript chars: 17010
- Keywords: argo, artifact, repository, commit, latest, artifacts, gitops, immutable, workflow, change, digest, flux, container, registry, application, actually, instead, manifest

### Resumo baseado na transcript

Uh bringing githops into the githops, bringing OCI into the GitOps world. I am co-founder and CTO of Acuity and co-creator of the Argo and Cargo project. Uh we're now using registries to distribute things like Helm charts uh WM modules, Lambda functions, policy bundles and and even machine learning u models these days. Um so if you think about container uh content delivery um networks it's the same idea except we're now extending this to um configuration um and if you need things like performance and redundancy um using things like registry mirrors caching layers um makes OCI distribution fast um scalable and redundant. And so let's compare how they might um trade off uh when considering versioning, packaging, security, delivery, and collaboration. uh with security and provenence um both OCI and git they have um strong integrity models.

### Excerpt da transcript

Hi everyone. Uh thanks for coming to this talk. Uh bringing githops into the githops, bringing OCI into the GitOps world. Uh my name is Jesse. I am co-founder and CTO of Acuity and co-creator of the Argo and Cargo project. Uh today we'll be exploring how OCI, which was originally built for containers, is now becoming a universal distribution format for all kinds of cloudnative artifacts. and what that means for GitOps. Uh so first a brief history of OCI. Uh so as you probably know Docker was the company that popularized uh containers but when containerizer uh was taking off it was a proprietary ecosystem and every platform had its own way of packaging and running containers and so it was a bit of a wild wild west. Um so in 2015 the industry got together uh to create the open container initiative um and its goal was about making docker images portable and consistent across runtimes so that the the same image could run anywhere and OCI standardized three core specs. um the image spec which is how a container is uh packaged, the runtime spec and how to actually run that image.

Uh and the distribution spec and this is how we push and pull artifacts uh via registries. Uh and this these three things gave us a foundation for container delivery. So fast forward to today um OCI isn't just about containers anymore. Uh we're now using registries to distribute things like Helm charts uh WM modules, Lambda functions, policy bundles and and even machine learning u models these days. So anything that can be be described as a package can be stored in versioned as OCI artifacts. So this opened up uh new opportunities for GitOps. Um with OCI we can now start deploying from OCI registries instead of git. Um we can promote immutable versions across your environments. Um and we can uh support offline and edge uh clusters where git uh cloning from git isn't ideal. So let's walk through a couple of these scenarios. So one place where OCI really shines is with uh disconnected environments. Um, so with GitOps, the git server is typically running from some centralized location. U but that git server might not be accessible in air gap clusters that aren't connected to the internet.

So instead of trying to sync from git servers, you can move OCR artifacts even through like uh USB drives um and load them into your private registry in your air gap um cluster. So it's the same delivery workflow just now airgapped. Another um use case is if you have edge or network constrained um locat
