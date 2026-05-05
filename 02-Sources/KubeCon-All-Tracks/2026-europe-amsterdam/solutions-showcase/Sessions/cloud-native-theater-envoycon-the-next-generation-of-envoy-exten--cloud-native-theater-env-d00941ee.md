---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Networking", "Storage Data"]
speakers: ["Rohit Agrawal", "Databricks"]
sched_url: https://kccnceu2026.sched.com/event/2EFzd/cloud-native-theater-envoycon-the-next-generation-of-envoy-extensibility-dynamic-modules-for-network-listener-and-http-filters-rohit-agrawal-databricks
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+The+Next+Generation+of+Envoy+Extensibility%3A+Dynamic+Modules+for+Network%2C+Listener%2C+and+HTTP+Filters+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | EnvoyCon: The Next Generation of Envoy Extensibility: Dynamic Modules for Network, Listener, and HTTP Filters - Rohit Agrawal, Databricks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Networking]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Rohit Agrawal, Databricks
- Schedule: https://kccnceu2026.sched.com/event/2EFzd/cloud-native-theater-envoycon-the-next-generation-of-envoy-extensibility-dynamic-modules-for-network-listener-and-http-filters-rohit-agrawal-databricks
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+The+Next+Generation+of+Envoy+Extensibility%3A+Dynamic+Modules+for+Network%2C+Listener%2C+and+HTTP+Filters+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | EnvoyCon: The Next Generation of Envoy Extensibility: Dynamic Modules for Network, Listener, and HTTP Filters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFzd/cloud-native-theater-envoycon-the-next-generation-of-envoy-extensibility-dynamic-modules-for-network-listener-and-http-filters-rohit-agrawal-databricks
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+The+Next+Generation+of+Envoy+Extensibility%3A+Dynamic+Modules+for+Network%2C+Listener%2C+and+HTTP+Filters+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ScMu2-ILhvg
- YouTube title: Cloud Native Theater | EnvoyCon: The Next Generation of Envoy Extensibility: Dynami... Rohit Agrawal
- Match score: 0.856
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-envoycon-the-next-generation-of-envoy-extensibili/ScMu2-ILhvg.txt
- Transcript chars: 12478
- Keywords: modules, envoy, dynamic, filters, write, latency, golang, module, extensions, traffic, process, policies, network, access, filter, support, balancing, arbback

### Resumo baseado na transcript

It's something that I've been deeply working and deeply involved for the last couple of quarters. I know I promised a live demo but that was before my talk got slashed in half. Uh but still like one of the important parts is there is always a cost. So anything you want to do tracing or anything which is not covered yet it's on the road map. So, Envoy was filtering the traffic and all these audit logs was being written on the disk as JSON because that's what we can do with envoy today. We had a Golang process which was reading these JSON logs, converting it to a proprietary proto and sending it onto the Kafka um Kafka streams and this was very latency prone.

### Excerpt da transcript

Uh so today I'm going to talk about envoy extensibility. It's something that I've been deeply working and deeply involved for the last couple of quarters. I know I promised a live demo but that was before my talk got slashed in half. So unfortunately no live demos today but I promise I'll do it um maybe even a better demo next time in the environ. So I'll talk you uh I'll talk through the dynamic modules. I'll walk you through some of the use cases that we have internally at data bricks which we are using dynamic modules for. So yeah, let's let's get started. So a quick intro. My name is Rohit Agarval. I work as a software engineer at data bricks at the traffic platform team. I'm a longtime Envoy user, contributor and more recently a maintainer. I've been contributing to Envoy for several years now. You might have seen some patches with matchers API like more recently dynamic modules and stuff like that. Uh there is a QR code on top of the screen that will take you to my LinkedIn profile. If you want to get connected after the talk, please feel free.

So before we start, just with a quick show of hands. How many of you are familiar with dynamic modules here? All right. Okay. A couple of people. So let's talk a little bit about envoy extensibility and how it changed over the years. So as you see like early 2017, we had something called Lua. It was good a scripting language. You can do small stuff like manipulate HTTP headers like basic stuff. uh very lightweight scripting it will do the job around mid 2019 we had was and then the entire entire picture of the extensibility changed uh it was a big deal it gave us a sandboxed multi-language runtime you could write was filters in rust go C++ you can compile them to was and envoway would run them in a VM um it supported stat sync http filters network filters access loggers the scope was much broader. Uh but still like one of the important parts is there is always a cost. You're running uh WASM as a VM. Uh which means that there's going to be serialization overhead when you pass the data across a boundary.

You can't zero copy access to headers and data. Uh and the sandbox it's great for security but it adds latency. Then if you look at it like Jan 2023 we introduced Golang HTTP filters. It became slightly more easier. Now you can write go code and you can write HTTP filters using that. Uh we started to get demands on can you add a network Golang filter, can you add a listener Golang filter. I think there were so
