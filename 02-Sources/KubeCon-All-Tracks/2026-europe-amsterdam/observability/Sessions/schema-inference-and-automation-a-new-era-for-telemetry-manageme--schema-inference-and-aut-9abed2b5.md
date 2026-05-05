---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Observability"
themes: ["AI ML", "Observability"]
speakers: ["Nicolas Takashi", "Coralogix", "Arthur Silva Sens", "Grafana Labs"]
sched_url: https://kccnceu2026.sched.com/event/2CVzR/schema-inference-and-automation-a-new-era-for-telemetry-management-nicolas-takashi-coralogix-arthur-silva-sens-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Schema+Inference+and+Automation%3A+A+New+Era+for+Telemetry+Management+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Schema Inference and Automation: A New Era for Telemetry Management - Nicolas Takashi, Coralogix & Arthur Silva Sens, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Nicolas Takashi, Coralogix, Arthur Silva Sens, Grafana Labs
- Schedule: https://kccnceu2026.sched.com/event/2CVzR/schema-inference-and-automation-a-new-era-for-telemetry-management-nicolas-takashi-coralogix-arthur-silva-sens-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Schema+Inference+and+Automation%3A+A+New+Era+for+Telemetry+Management+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Schema Inference and Automation: A New Era for Telemetry Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzR/schema-inference-and-automation-a-new-era-for-telemetry-management-nicolas-takashi-coralogix-arthur-silva-sens-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Schema+Inference+and+Automation%3A+A+New+Era+for+Telemetry+Management+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vSW29xvdq1A
- YouTube title: Schema Inference and Automation: A New Era for Telemetry Mana... Nicolas Takashi & Arthur Silva Sens
- Match score: 0.855
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/schema-inference-and-automation-a-new-era-for-telemetry-management/vSW29xvdq1A.txt
- Transcript chars: 32899
- Keywords: environment, variable, instrumentation, little, easier, explain, harder, interface, chooses, weaver, observability, prometheus, schema, metrics, generate, metric, client, design

### Resumo baseado na transcript

I lead the Prometheus special interest group in Open Telemetry community together with Dave David Ashpole. I'm observability stack leader at Coralogix and I'm Perseus maintainer and I've been working in some observability related projects at CNCF like Thanos, Prometheus, and Open Telemetry as well. Uh so, Observability by Design is um is something that Weaver is created to. For example Prometheus conventions requires that the unit is units are uh suffix in the in the metric name. If you have other kinds of very custom uh uh policies that you need for your org, uh Weaver is a design for this. You can do instrumentation, you can do dashboards, you can do alerts, like literally anything that you imagine.

### Excerpt da transcript

Hello everybody, thanks for being here. Our talk is called schema inference automation. Although we do have inference in the title is not AI related. I'm sorry if that's all your expectation. That was not intentional. Uh But anyway I'm Arthur Silva Sense. I'm a software engineer at Grafana Labs. I'm also a Prometheus maintainer. I lead the Prometheus special interest group in Open Telemetry community together with Dave David Ashpole. And hello folks. My name is Nico Takash. I'm observability stack leader at Coralogix and I'm Perseus maintainer and I've been working in some observability related projects at CNCF like Thanos, Prometheus, and Open Telemetry as well. Thanks for being here. Yeah, but we are not talking about Perseus or Prometheus today. We're talking about a tool called Open Telemetry Weaver. Uh who here has heard about Weaver before? Oh, that's actually More than 30 people. That's cool. And have you besides hearing about it, have you tried? Okay, that's a little less. >> it's Uh I mean I I mean I tried myself.

Uh I think uh we [snorts] watched a talk uh in Observability Day in 2024 if I'm not mistaken, which is called Observability by Design. Sign. Um this is the QR code for the recording if you would like to understand more what is Weaver. And the concept of Observability by Design. >> Yeah, yeah, and the concept of Observability by Design. There's also another talk that happened yesterday during the Observability Day uh by Benedict and Sebastian. Say hello. Yeah. All right, yeah. Sorry. [laughter] Uh yeah, this is the link also for the their talk. They showed how um Observability They talked more about a schema, not necessarily about Weaver, but how Shopify is using uh schemas to to automate a lot of things in the Observability space. And uh that brings me one question. I Who here likewise Shopify has a team of 20 20 engineers? Is that correct? Only working on Observability. >> Only for Observa- Observability. One, two. Three. With Shopify, yeah. Okay. Yeah, I I think like in reality the Observability by Design is great, but uh we are going to talk about how to go into this place when you are not You don't have like a superstar team.

That's how That's how it bad, but that's not what I meant. Uh well, so okay. Uh what is Observability by Design? So, it's when you treat uh your Telemetry like an API. Oh, you have a document that declares how things look like and you could from this declarative uh uh file, you can do all sorts of things like
