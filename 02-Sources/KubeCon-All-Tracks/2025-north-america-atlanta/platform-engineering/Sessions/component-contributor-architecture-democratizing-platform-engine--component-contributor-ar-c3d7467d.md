---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering", "Community Governance"]
speakers: ["Anoop Gopalakrishnan", "Jerome Guionnet", "Guidewire"]
sched_url: https://kccncna2025.sched.com/event/27Fb4/component-contributor-architecture-democratizing-platform-engineering-with-cncf-projects-anoop-gopalakrishnan-jerome-guionnet-guidewire
youtube_search_url: https://www.youtube.com/results?search_query=Component+Contributor+Architecture%3A+Democratizing+Platform+Engineering+With+CNCF+Projects+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Component Contributor Architecture: Democratizing Platform Engineering With CNCF Projects - Anoop Gopalakrishnan & Jerome Guionnet, Guidewire

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Anoop Gopalakrishnan, Jerome Guionnet, Guidewire
- Schedule: https://kccncna2025.sched.com/event/27Fb4/component-contributor-architecture-democratizing-platform-engineering-with-cncf-projects-anoop-gopalakrishnan-jerome-guionnet-guidewire
- Busca YouTube: https://www.youtube.com/results?search_query=Component+Contributor+Architecture%3A+Democratizing+Platform+Engineering+With+CNCF+Projects+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Component Contributor Architecture: Democratizing Platform Engineering With CNCF Projects.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fb4/component-contributor-architecture-democratizing-platform-engineering-with-cncf-projects-anoop-gopalakrishnan-jerome-guionnet-guidewire
- YouTube search: https://www.youtube.com/results?search_query=Component+Contributor+Architecture%3A+Democratizing+Platform+Engineering+With+CNCF+Projects+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0yW79y48U3k
- YouTube title: Component Contributor Architecture: Democratizing Platform... Anoop Gopalakrishnan & Jerome Guionnet
- Match score: 0.772
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/component-contributor-architecture-democratizing-platform-engineering/0yW79y48U3k.txt
- Transcript chars: 25959
- Keywords: component, application, platform, create, developer, everything, staging, expert, snorts, provide, single, deploy, creating, engineering, runtime, microservices, version, needed

### Resumo baseado na transcript

I know it's been a long day for many of you guys and uh giving us your brain for this period of time. Um to start off with this presentation um you know component contributor architecture democratizing platform engineering. Um there's a lot of compliance demands on us as a provider as well in addition to the performance requirements for these uh these systems, right? uh but today we're going to focus majorly on how our Kubernetes and workload platforms work and we've been building the platform since 2018 and I have uh I've worked in prior companies before so it's been a decade of building platforms. Uh, and we've faced the same issues because our backlogs are mile long. What if we democratize that entire model in such a way that an application team for example who knows a lot about open search if we give them a guardrail around you know this is how you can maintain that component yourself but also provide

### Excerpt da transcript

Hello everyone. Thank you for taking this time. I know it's been a long day for many of you guys and uh giving us your brain for this period of time. Really appreciate uh you being here. So sorry. Okay. Um to start off with this presentation um you know component contributor architecture democratizing platform engineering. It's a mouthful. I we we put it there on p purpose. I hope somebody you know sticks to it. U but before we start anything can we get a quick show of hand of how many people are building internal development platforms on Kubernetes just like I thought who isn't exactly as we thought. Okay so we're starting a little bit of introduction. My name is Anup. I work as a vice president of engineering for Guideire Software. Um, if you don't know what Guidewire is, you know, think insurance. Most likely your policies are done by an insured provider who potentially uses our software. And sorry California guys, we are not the reason for the price increases. And I have with me Jerome, you know. >> So, hi everyone.

So, I'm Jerome. I'm a chief architect. I'm working for Anoop. Um yeah so we are building the the platform for guidewire that is used by our developer but also by our insurer and we will go through this journey um through different generation evolution with yeah so setting the scene on what guide does uh we provide a software platform and on top of that we also provide a runtime platform uh for our customers. We have some of our customers right here sitting next to us. Copper points there. Glad to see you guys. Um, but it is all built on Kubernetes and we are present in all these regions. We have our clusters across these 140 customers, 140 plus customers. And you might be thinking, oh that's nothing. We talk about thousands of microservices. 140 customers don't seem like anything. But trust me, each one of these are huge monolets. And we run the entire enchilada from monoliths to microservices to functions as a service and insurance companies. We are um are highly regulated. Um there's a lot of compliance demands on us as a provider as well in addition to the performance requirements for these uh these systems, right?

We run pabates pabyte scale data lakes. uh but today we're going to focus majorly on how our Kubernetes and workload platforms work and we've been building the platform since 2018 and I have uh I've worked in prior companies before so it's been a decade of building platforms. One thing that has always hit us is you know ever
