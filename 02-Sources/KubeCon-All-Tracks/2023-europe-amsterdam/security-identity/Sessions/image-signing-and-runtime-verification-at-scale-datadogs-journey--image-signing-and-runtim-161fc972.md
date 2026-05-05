---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security", "Storage Data", "Runtime Containers", "SRE Reliability"]
speakers: ["Ethan Lowman", "Datadog"]
sched_url: https://kccnceu2023.sched.com/event/1HyX1/image-signing-and-runtime-verification-at-scale-datadogs-journey-ethan-lowman-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Image+Signing+and+Runtime+Verification+at+Scale%3A+Datadog%27s+Journey+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Image Signing and Runtime Verification at Scale: Datadog's Journey - Ethan Lowman, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]], [[Storage Data]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ethan Lowman, Datadog
- Schedule: https://kccnceu2023.sched.com/event/1HyX1/image-signing-and-runtime-verification-at-scale-datadogs-journey-ethan-lowman-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Image+Signing+and+Runtime+Verification+at+Scale%3A+Datadog%27s+Journey+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Image Signing and Runtime Verification at Scale: Datadog's Journey.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyX1/image-signing-and-runtime-verification-at-scale-datadogs-journey-ethan-lowman-datadog
- YouTube search: https://www.youtube.com/results?search_query=Image+Signing+and+Runtime+Verification+at+Scale%3A+Datadog%27s+Journey+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=g7xgBzZ3t_A
- YouTube title: Image Signing and Runtime Verification at Scale: Datadog's Journey - Ethan Lowman, Datadog
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/image-signing-and-runtime-verification-at-scale-datadogs-journey/g7xgBzZ3t_A.txt
- Transcript chars: 27780
- Keywords: signing, verification, images, signature, container, registry, signatures, verify, metadata, datadog, runtime, approach, pretty, public, cluster, signed, actually, features

### Resumo baseado na transcript

thank you all for coming my name is Ethan and I'm going to be talking about how we're signing and verifying container images in a kubernetes environment a datadog so this is a talk about datadog's internal infrastructure but this infrastructure ultimately supports the datadoc product which is a an observability and security platform we run at a very high scale and I have a few numbers on this on this slide to illustrate that but the important thing to remember for this talk is that we run on self-hosted

### Excerpt da transcript

thank you all for coming my name is Ethan and I'm going to be talking about how we're signing and verifying container images in a kubernetes environment a datadog so this is a talk about datadog's internal infrastructure but this infrastructure ultimately supports the datadoc product which is a an observability and security platform we run at a very high scale and I have a few numbers on this on this slide to illustrate that but the important thing to remember for this talk is that we run on self-hosted kubernetes so you have hundreds of clusters tens of thousands of nodes and hundreds of thousands of pods so the solution that we we designed for signing and verifying images needs to work at that scale but about me my name is Ethan I'm a senior software engineer at datadog where I've been working on infrastructure security for about four years now so if you have any questions um about the talk feel free to approach me afterwards or you can reach me at the address on this slide so why should we care about signing and verifying images on the slide I have a simplified model of what an internal software supply chain looks like targeting a kubernetes environment so it has all the components you'd expect Version Control CI CD container registry and then the various components of kubernetes but as as an organization matures each of these stages is often served by multiple sub services and as the complexity grows this means that you have more surface area that you need to secure and each of these stages is is a target for malicious code injection so an attacker could inject a malicious payload at any stage in this Pipeline and that might reach prod eventually allowing that code to run even if the attacker doesn't have direct production access so what signing and verifying images gets us is a guarantee of provenance so if we sign an image in CI and then verify it in one or more Downstream systems what this provides us is a guarantee from the perspective of the verifier that the image that it's handling is bid for bit the same as the image that was built and signed in continuous integration so the overall goal is to push signing as far as possible to the left as close to build time as possible and push verification as far as possible to the right as close to run time as possible to to extend the scope of the Integrity guarantee of that signature in the past there have been a variety of approaches to assigning container images but the ones that have achieved the best
