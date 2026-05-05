---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Toddy Mladenov", "Flora Taagen", "Dallas Delaney", "Microsoft"]
sched_url: https://kccnceu2026.sched.com/event/2EF6H/beyond-image-pull-time-ensuring-runtime-integrity-with-image-layer-signing-toddy-mladenov-flora-taagen-dallas-delaney-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+Image+Pull-Time%3A+Ensuring+Runtime+Integrity+With+Image+Layer+Signing+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Beyond Image Pull-Time: Ensuring Runtime Integrity With Image Layer Signing - Toddy Mladenov, Flora Taagen & Dallas Delaney, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Toddy Mladenov, Flora Taagen, Dallas Delaney, Microsoft
- Schedule: https://kccnceu2026.sched.com/event/2EF6H/beyond-image-pull-time-ensuring-runtime-integrity-with-image-layer-signing-toddy-mladenov-flora-taagen-dallas-delaney-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+Image+Pull-Time%3A+Ensuring+Runtime+Integrity+With+Image+Layer+Signing+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Beyond Image Pull-Time: Ensuring Runtime Integrity With Image Layer Signing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6H/beyond-image-pull-time-ensuring-runtime-integrity-with-image-layer-signing-toddy-mladenov-flora-taagen-dallas-delaney-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Beyond+Image+Pull-Time%3A+Ensuring+Runtime+Integrity+With+Image+Layer+Signing+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2WhADdlb_pA
- YouTube title: Beyond Image Pull-Time: Ensuring Runtime Integrit...  Toddy Mladenov, Flora Taagen & Dallas Delaney
- Match score: 0.783
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/beyond-image-pull-time-ensuring-runtime-integrity-with-image-layer-sig/2WhADdlb_pA.txt
- Transcript chars: 21683
- Keywords: container, layers, actually, runtime, manifest, certificate, signature, kernel, signing, notary, registry, verification, artifacts, verify, pulled, individual, cached, dmverity

### Resumo baseado na transcript

I'm one of the maintainers of notary project and today we have a interesting topic uh that will be delivered by Flora and Dallas. Flora and Dallas are new contributors to the project and they'll talk about uh uh image layer signing. And so this introduces a security risk where a attacker or a malicious actor, you know, if given or gaining uh access to the host could be able to modify one of those cached image layers. And this problem intensifies in multi-tenant environments where layer sharing across multiple containers and applications is common. So now we're going to show just a very short demo of that potential attack scenario. Um and I'm going to pass it off to Dallas now uh to walk us through a demo.

### Excerpt da transcript

Uh I am Tony. I'm one of the maintainers of notary project and today we have a interesting topic uh that will be delivered by Flora and Dallas. Flora and Dallas are new contributors to the project and they'll talk about uh uh image layer signing. So looking forward to that. Uh very quickly for folks who are not familiar with notary project what notary project is it's um a project in CNCF which is for uh supply chain security. Uh we have two sub kind of projects or tools under notary project. One is the notation CLI that is used for signing OCI artifacts any kind of artifacts like container images sbombs helm charts. Uh you can use the CLI. There are also libraries uh that you can use if you need to do more custom integration into your tooling. And the second project is called Ratify which is external data provider for uh OPAI gatekeeper and can be used for admission control. Uh you can verify images that are signed with uh notation CLI and uh also you can use them to verify images that are signed with uh cosign or six door infrastructure.

uh notary project is used by uh various companies. Uh we are from Microsoft but also AWS is using it. Alibaba cloud uh you can see a bunch of logos there. So uh without any further ado I'll pass it to Flora and Dallas so they can go to more interesting part of the presentation. Thank you. >> Perfect. Thanks Toddy. Um so to begin we want to walk through what the existing signing process looks like for signing containers with the notary project today. Um it all starts with the image build phase. So this is when you are building a container image. Maybe you're using tools like docker or github actions. And at this stage your container image has not been signed. Then we enter the image signing phase. This is when the notary project actually steps in to sign your image manifest digest. Uh this creates a cryptographic signature that will bind the signer's identity to the image manifest itself. Then that signature gets pushed. It gets stored as a separate OCI referral artifact um in your container registry alongside the container image.

Um, and then finally we enter the pull time verification step. So when someone wants to pull their image down to the host, the signature gets verified against the image manifest digest to confirm that the image hasn't been modified, it hasn't been tampered with, um, and it's coming from a trusted signer. So you might have noticed that the notary project today is signing at the manifest level an
