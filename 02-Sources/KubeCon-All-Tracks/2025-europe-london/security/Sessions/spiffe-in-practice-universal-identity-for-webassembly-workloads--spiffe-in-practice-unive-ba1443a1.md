---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["Security", "Runtime Containers"]
speakers: ["Joonas Bergius", "Cosmonic", "Colin Murphy", "Adobe"]
sched_url: https://kccnceu2025.sched.com/event/1tx8U/spiffe-in-practice-universal-identity-for-webassembly-workloads-joonas-bergius-cosmonic-colin-murphy-adobe
youtube_search_url: https://www.youtube.com/results?search_query=%E2%80%8B%E2%80%8BSPIFFE+in+Practice%3A+Universal+Identity+for+WebAssembly+Workloads+CNCF+KubeCon+2025
slides: []
status: parsed
---

# ​​SPIFFE in Practice: Universal Identity for WebAssembly Workloads - Joonas Bergius, Cosmonic & Colin Murphy, Adobe

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Runtime Containers]]
- País/cidade: United Kingdom / London
- Speakers: Joonas Bergius, Cosmonic, Colin Murphy, Adobe
- Schedule: https://kccnceu2025.sched.com/event/1tx8U/spiffe-in-practice-universal-identity-for-webassembly-workloads-joonas-bergius-cosmonic-colin-murphy-adobe
- Busca YouTube: https://www.youtube.com/results?search_query=%E2%80%8B%E2%80%8BSPIFFE+in+Practice%3A+Universal+Identity+for+WebAssembly+Workloads+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre ​​SPIFFE in Practice: Universal Identity for WebAssembly Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8U/spiffe-in-practice-universal-identity-for-webassembly-workloads-joonas-bergius-cosmonic-colin-murphy-adobe
- YouTube search: https://www.youtube.com/results?search_query=%E2%80%8B%E2%80%8BSPIFFE+in+Practice%3A+Universal+Identity+for+WebAssembly+Workloads+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=c0dEL_bBRVU
- YouTube title: ​​SPIFFE in Practice: Universal Identity for WebAssembly Workloads - Joonas Bergius & Colin Murphy
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/spiffe-in-practice-universal-identity-for-webassembly-workloads/c0dEL_bBRVU.txt
- Transcript chars: 25493
- Keywords: spiffy, assembly, identity, little, actually, running, important, secure, bedrock, workloads, docker, working, workload, potentially, component, purposes, essentially, components

### Resumo baseado na transcript

this uh welcome to spiffy in practice web assembly web assembly identity for web um sorry universal identity for web assembly workloads. So I'm going to take you back to a really pleasant time for all of us, March 2020. Fed Ramp in March of 2021 will require security scans for CVEes, right? I haven't been in the Kubernetes space really for four years but you know um with between our applications and the various parts of Kubernetes and uh we do scans we use J J J J J J J J J J J J J Uh, and um, and then two, uh, I'm kind of done personally with Docker and in a way Kubernetes. If if we're going to have workloads where the data is, if we're going to have low latency for our customers, if we're going to have a really good application experience, I'm not going to want to manage, you know, 30 to 40 separate Kubernetes clusters individually.

### Excerpt da transcript

this uh welcome to spiffy in practice web assembly web assembly identity for web um sorry universal identity for web assembly workloads. That'll be the last time I make a mistake. Um my name is Colin Murphy. I'm a senior Rust engineer at Adobe. I'm Jonas. Um I'm Jonas Vio. I'm a um senior software engineer at Cosmonic. And we're both WAMOM cloud maintainers. All right. So I'm going to take you back to a really pleasant time for all of us, March 2020. And [Music] um this is the origin story of my interest both in serverside web assembly and um my appreciation for spiffy. Um at the time I was the manager for Adobe document cloud's infrastructure um for services. Um and my number one uh priority at the time was uh Adobe Sign for GovCloud. Um we had dozens of microservices. Probably many of you are familiar with this kind of story. Dozens of microservices. Uh they were HIPPA, SOCK 2, PCI, you name it compliant. But Fed Ramp is is a very different ballgame. Um, and uh, we'd been using ISTTO. I'm very I'm always trying to, you know, use things that don't work yet.

So, I was using, uh, ISTTO 1.0 in 2018. I'd been using it for a while. Um, uh, and we needed FIPS 140-2 compliance. So, I needed a vendor. I needed somebody to contractually, uh, do that. And they, they stepped up. They did it. It was great. But, there was a problem. Um, and that's uh we didn't have Adobe's identity management system that's that couldn't go to Fed Ramp with us uh to our government cloud. Um, and uh we have at Adobe we have the IMS we still do to this day. uh inter you know identity management system originally created for entitlements for people to use our products uh prevent py you know piracy um uh but we also use that for service to service calls which not great um but we couldn't bring that with us um and so we really this is the first time I really got to use spiffy um solo IO had this agent this little uh RPM I could install on our non containerized workloads and uh everything just got integrated in really nicely with the stack. So I was I was really happy. Um so everything was going really well.

Look at all of our containers. Everybody's moving in the same direction. Uh everything's going according to plan. And then right yes uh so received some very bad news. Fed Ramp in March of 2021 will require security scans for CVEes, right? Uh crit critical vulnerabil vulner CVS. Does anybody know what that is? Critical vulnerabilities and exceptions. Um you know, uh vulnerabilities usu
