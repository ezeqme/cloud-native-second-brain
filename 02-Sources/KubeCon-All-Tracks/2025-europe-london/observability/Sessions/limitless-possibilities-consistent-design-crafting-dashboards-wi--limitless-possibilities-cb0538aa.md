---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Observability"
themes: ["Observability"]
speakers: ["Nicolas Takashi", "Coralogix", "Antoine Thébaud", "Amadeus"]
sched_url: https://kccnceu2025.sched.com/event/1txHy/limitless-possibilities-consistent-design-crafting-dashboards-with-perses-dac-nicolas-takashi-coralogix-antoine-thebaud-amadeus
youtube_search_url: https://www.youtube.com/results?search_query=Limitless+Possibilities%2C+Consistent+Design%3A+Crafting+Dashboards+With+Perses+DAC+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Limitless Possibilities, Consistent Design: Crafting Dashboards With Perses DAC - Nicolas Takashi, Coralogix & Antoine Thébaud, Amadeus

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Nicolas Takashi, Coralogix, Antoine Thébaud, Amadeus
- Schedule: https://kccnceu2025.sched.com/event/1txHy/limitless-possibilities-consistent-design-crafting-dashboards-with-perses-dac-nicolas-takashi-coralogix-antoine-thebaud-amadeus
- Busca YouTube: https://www.youtube.com/results?search_query=Limitless+Possibilities%2C+Consistent+Design%3A+Crafting+Dashboards+With+Perses+DAC+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Limitless Possibilities, Consistent Design: Crafting Dashboards With Perses DAC.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txHy/limitless-possibilities-consistent-design-crafting-dashboards-with-perses-dac-nicolas-takashi-coralogix-antoine-thebaud-amadeus
- YouTube search: https://www.youtube.com/results?search_query=Limitless+Possibilities%2C+Consistent+Design%3A+Crafting+Dashboards+With+Perses+DAC+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7h70Olo5Uzk
- YouTube title: Limitless Possibilities, Consistent Design: Crafting Dashboards... Nicolas Takashi & Antoine Thébaud
- Match score: 0.868
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/limitless-possibilities-consistent-design-crafting-dashboards-with-per/7h70Olo5Uzk.txt
- Transcript chars: 25105
- Keywords: dashboard, dashboards, creating, plugins, question, provide, golang, basically, panels, source, preview, definition, github, support, import, export, observability, process

### Resumo baseado na transcript

Uh I'm observability tech leads at Corora Logix and I'm Promeus operator and process maintainer and I like to pushing code on other projects like tennos, open telemetry, promeus. I'm a senior software engineer at Amadius working on an observability platform and a process maintainer for quite some years now. Uh but anyway with yeah so with this plug-in architecture really we we uh we allow anyone any team any anything to provide to create their own plugins to extend the capabilities of pers. So it's actually quite easy to just output the dashboard in the format of CRS that you can uh push to Kubernetes thanks to the pers operator that we provide. Uh and so the data model is quite clean and familiar for Kubernetes users. But if you are curious the QR code we shared uh earlier so it was a bit fast but you will be able to to recover it later uh it is due to the demo project for for this demo and there is both Q and go dashboard so you can have a look uh at both SDKs.

### Excerpt da transcript

So hello hello everyone. Um thank you for being here. Uh it's a crowded room. Yeah, we have some lights here but yeah we can see everyone. So um thank you for having us. I hope you enjoy. Uh and let's get started. So Antoine. Yeah sure. So yeah first quick question. Have anyone heard about Pers yet? And who knows a bit what it's about? Okay. Not that quite a few people. Yeah. Yeah, cool. So before we getting started, who we are? Uh my name is Nicholas Takash. Uh I'm observability tech leads at Corora Logix and I'm Promeus operator and process maintainer and I like to pushing code on other projects like tennos, open telemetry, promeus. So mostly CNCF related observability ecosystem. Yeah. And I'm Antoan Tu. I'm a senior software engineer at Amadius working on an observability platform and a process maintainer for quite some years now. Cool. Let's go. Yes. So first uh few words about pers in general then we will dive into the specific to topic of today. So Pers it's an observability visualization tool and you have an overview of it of its let's say maini the dashboard UI here on the screen.

So it's an Apache 2 licensed project and recently so summer last year it made it to the CNCF uh so as a sandbox project and for these reasons uh we really see pers so besides let's say the really the it part uh as a standalone application that you can deploy we really see it also as an an initiative to converge towards an open specification and standard specification for dashboards in general. general so and hopefully to increase interoper interoperability between various observability tools. So pers has various main focuses that we will go through quickly. So first extensibility. So, Pers comes with a plug-in architecture that basically has been around for quite some time, but we have a brand new architecture coming, a V2 uh by uh yeah, the coming in the next weeks. So, the objective was to release that before CubeCon, but yeah, sorry we failed on that. Uh but anyway with yeah so with this plug-in architecture really we we uh we allow anyone any team any anything to provide to create their own plugins to extend the capabilities of pers.

So could be in terms of v visualization options and also in terms of data sources. It's also uh pers is also embeddable in the sense that it provides a set of npm packages that you can embed in your own UI. So this is for example the case of the open shift console by redat which is uh one of the main contributor of persus. So they embed
