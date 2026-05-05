---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["Observability"]
speakers: ["Victoria Nduka", "Independent", "Amy Super", "Grafana Labs"]
sched_url: https://kccncna2025.sched.com/event/27FZr/ux-research-report-prometheus-and-otels-resource-attributes-victoria-nduka-independent-amy-super-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=UX+Research+Report%3A+Prometheus+and+OTel%27s+Resource+Attributes.+CNCF+KubeCon+2025
slides: []
status: parsed
---

# UX Research Report: Prometheus and OTel's Resource Attributes. - Victoria Nduka, Independent & Amy Super, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Atlanta
- Speakers: Victoria Nduka, Independent, Amy Super, Grafana Labs
- Schedule: https://kccncna2025.sched.com/event/27FZr/ux-research-report-prometheus-and-otels-resource-attributes-victoria-nduka-independent-amy-super-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=UX+Research+Report%3A+Prometheus+and+OTel%27s+Resource+Attributes.+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre UX Research Report: Prometheus and OTel's Resource Attributes..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZr/ux-research-report-prometheus-and-otels-resource-attributes-victoria-nduka-independent-amy-super-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=UX+Research+Report%3A+Prometheus+and+OTel%27s+Resource+Attributes.+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cSLXIAc020A
- YouTube title: UX Research Report: Prometheus and OTel's Resource Attributes. - Victoria Nduka & Amy Super
- Match score: 0.905
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/ux-research-report-prometheus-and-otels-resource-attributes/cSLXIAc020A.txt
- Transcript chars: 20345
- Keywords: attributes, resource, prometheus, actually, research, victoria, documentation, recommendations, better, approach, understand, communities, changes, metric, mentorship, everything, target, another

### Resumo baseado na transcript

Um this talk is a UX research report where we'll talk about um how should Prometheus handle open telemetry resource attributes. Uh I'm also uh involved with the open telemetry contributor experience SIG. Uh but it wasn't really exactly clear how to solve this or what the key problems were. That said, it was also really important for us to learn what stakeholders in the communities felt uh for a couple of reasons. So, I'm going to pass this to Victoria via video if the demo guides, you know, work and the video worked. And the only thing I may want to add is if you want to learn more about me and my work, you should check out my website varandoka.org.

### Excerpt da transcript

Thank you all for joining today. Um this talk is a UX research report where we'll talk about um how should Prometheus handle open telemetry resource attributes. Just a quick introduction. Uh my name is Amy Super. I'm a product designer at Graphana Labs. Uh I'm also uh involved with the open telemetry contributor experience SIG. While I'm here presenting, the real leader of this project is Victoria Enuka. Victoria is a UX designer researcher. She's also a technical writer and she is involved in the open telemetry end user SIG and also getting involved in the Prometheus community. I met Victoria through a Linux foundation and CNCF mentorship program where I served as mentee or I'm sorry I served as mentor and Victoria was our mentee. Our other mentors were Arthur who's a developer at Graphana Labs. He's a Prometheus maintainer, also hangs out with the hotel community and Andre who is a researcher at Graphfana Labs uh and also involved in the open telemetry end user segment. So for a little bit of background, why did we do this project?

It was becoming more apparent in recent months to the Prometheus community that end users were struggling to deal with open telemetry resource attributes. There were some sort of odds and ends of feedback coming in things about um the query experience being bad. People were concerned about high cardality issues. Uh but it wasn't really exactly clear how to solve this or what the key problems were. So we set out to learn more as part of this mentorship. These are our research goals. Hopefully, you can read them from there. Uh, but I want to actually talk about what's not on this slide, which is we did not conduct user research to determine how our end users should use our tools. Um, it's something that I heard as we sort of gave our recommendations was like, you know, well, they should be doing this. And the reason we do UX research is to understand the reality of the situation, understand how people are using those tools today. and then that way we can hopefully um make improvements to meet them where they are.

So um just want to call that out there. But but overall our goals were really sort of just understanding what the pain points were such that we could make better recommendations. That said, it was also really important for us to learn what stakeholders in the communities felt uh for a couple of reasons. One was to learn the context of why we ended up where we are today. Uh but the other and probably just as important
