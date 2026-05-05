---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["Security"]
speakers: ["John Kjell", "ControlPlane"]
sched_url: https://kccncna2025.sched.com/event/27Fap/safely-sourcing-oss-beyond-0-cves-john-kjell-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=Safely+Sourcing+OSS+-+Beyond+0+CVEs+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Safely Sourcing OSS - Beyond 0 CVEs - John Kjell, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Atlanta
- Speakers: John Kjell, ControlPlane
- Schedule: https://kccncna2025.sched.com/event/27Fap/safely-sourcing-oss-beyond-0-cves-john-kjell-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=Safely+Sourcing+OSS+-+Beyond+0+CVEs+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Safely Sourcing OSS - Beyond 0 CVEs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fap/safely-sourcing-oss-beyond-0-cves-john-kjell-controlplane
- YouTube search: https://www.youtube.com/results?search_query=Safely+Sourcing+OSS+-+Beyond+0+CVEs+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hxtSzRB9FtY
- YouTube title: Safely Sourcing OSS - Beyond 0 CVEs - John Kjell, ControlPlane
- Match score: 0.813
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/safely-sourcing-oss-beyond-0-cves/hxtSzRB9FtY.txt
- Transcript chars: 26108
- Keywords: source, security, projects, software, around, little, compliance, better, vulnerabilities, working, images, support, actually, problems, understand, maintainer, maintainers, foundation

### Resumo baseado na transcript

Uh I had a very lengthy travel journey myself on Saturday night into very early Sunday morning. Uh hopefully we all have safe travels that are as fast as possible uh in the next couple days going home. uh and I'm also a co-chair for the CNCF's technical advisory group for security and compliance uh and try to be active and contribute as many places I as I can across the the CNCF and open SSF. But also the cost of rebuilding what exists in open source would be in this case for most people four times as expensive as just using open source. Um the Kubernetes only supports uh it three four major uh versions backwards. So in [sighs] the end, your open- source project that you loved, that you used, that solved all of your actual userfacing problems that you didn't invest in, you didn't support, you didn't contribute to because you just bought a zero CV image from somewhere else.

### Excerpt da transcript

Thank you everybody for coming. Um I am grateful that you've all made it here. Uh I had a very lengthy travel journey myself on Saturday night into very early Sunday morning. Uh hopefully we all have safe travels that are as fast as possible uh in the next couple days going home. Uh but we're going to talk about safely sourcing uh open source software kind of trying to understand beyond zero CVEes. So, as we kick this off, um before we get started, just a little bit um about me, uh set expectations really high to start out with. Uh two-time college dropout, so um you know, things all things are possible. I was a former world leader, who's the most amazing job title ever. Uh that was when I was in charge of the bike department at Toys R Us. So, um they called the different areas in the store worlds. So, I got to be a world leader. Um, currently I'm a security consultant at control plane. Uh, I'm also an open- source maintainer uh for the Entto project, a couple of sub projects, Witness and Archavista.

Uh, and then in the open SSF, the Sbombit project and the update framework. Um, we just had the 10-year birthday for Intto. Uh, so that's I've not been working on it for 10 years, but uh, it's it's awesome to kind of see that milestone. uh and I'm also a co-chair for the CNCF's technical advisory group for security and compliance uh and try to be active and contribute as many places I as I can across the the CNCF and open SSF. So this is the abstract that was in the session here. Um it's a bit dry. It's a bit boring probably. I'm a little surprised you all showed up here. Uh so rather than taking this abstract and just making it concrete and telling you the details of everything, uh I'd like to tell you a story instead. Uh and before I get started, I have to put a little disclaimer here. Um that this is a fictitious example. Um the all the characters in this I actually have played that role myself. whether it's uh an open- source maintainer uh consumer of open source or a vendor that sells zero CVE images.

Uh we only as a company sell zero CV images for the Flux project, not everything. Um so any uh thing that you see that that mimics real life too much is purely coincidental. So there are demons in the world, right? all these things that we have to overcome whether they're absurd customer requirements or delivery deadlines or budget cuts. Nobody here has ever been asked to do more with less, have they? Maybe. So, how do we deal with this? How do we deliver
