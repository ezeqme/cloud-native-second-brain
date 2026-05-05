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
themes: ["AI ML", "Observability", "Networking", "SRE Reliability", "Community Governance"]
speakers: ["Eduardo Silva", "Chronosphere | A Palo Alto Networks Company"]
sched_url: https://kccnceu2026.sched.com/event/2EF65/fluent-bit-v5-pushing-the-limits-of-observability-at-scale-eduardo-silva-chronosphere-a-palo-alto-networks-company
youtube_search_url: https://www.youtube.com/results?search_query=Fluent+Bit+V5%3A+Pushing+the+Limits+of+Observability+at+Scale+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Fluent Bit V5: Pushing the Limits of Observability at Scale - Eduardo Silva, Chronosphere | A Palo Alto Networks Company

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Networking]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Eduardo Silva, Chronosphere | A Palo Alto Networks Company
- Schedule: https://kccnceu2026.sched.com/event/2EF65/fluent-bit-v5-pushing-the-limits-of-observability-at-scale-eduardo-silva-chronosphere-a-palo-alto-networks-company
- Busca YouTube: https://www.youtube.com/results?search_query=Fluent+Bit+V5%3A+Pushing+the+Limits+of+Observability+at+Scale+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Fluent Bit V5: Pushing the Limits of Observability at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF65/fluent-bit-v5-pushing-the-limits-of-observability-at-scale-eduardo-silva-chronosphere-a-palo-alto-networks-company
- YouTube search: https://www.youtube.com/results?search_query=Fluent+Bit+V5%3A+Pushing+the+Limits+of+Observability+at+Scale+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=w1pj0Lz1mW4
- YouTube title: Fluent Bit V5: Pushing the Limits of Observability at Scale - Eduardo Silva
- Match score: 0.972
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/fluent-bit-v5-pushing-the-limits-of-observability-at-scale/w1pj0Lz1mW4.txt
- Transcript chars: 40125
- Keywords: fluent, processing, always, sampling, collector, question, pipeline, attributes, logs, processor, performance, resource, actually, traces, server, better, processors, course

### Resumo baseado na transcript

My name is Eduardo and the presentation today is around pushing the limits on the fluent bit project. But if you are new or just are getting started on this, please raise your hand so I can Oh, you all if you're using it. So it's not just to receive over the network but also from the local system even systemd if you want to process systemd lock logs from your Linux box you can use this type and for processor which allow you to modify the data or enrich it we have Lua scripting so you can have your Lua scripts in your configuration we have Kubernetes metadata enrichment sampling for traces and we have more than a hundred right but this is the general idea and enroing is like what type of you are deploying this in production sometimes you get problems right or the data is not flowing there's a network error so you can understand okay where the problem could be could be in the network when fluent bit is trying to reach an endpoint We have safety around buffering and buffering with storage in the file system.

### Excerpt da transcript

My name is Eduardo and the presentation today is around pushing the limits on the fluent bit project. I assume that some of you know the project. But if you are new or just are getting started on this, please raise your hand so I can Oh, you all if you're using it. Perfect. Okay, we have I need to justify my first slides, right? Because we're going to get back to the basics. But um well I started this break many years ago. We are from the fluenty team and really happy to have this opportunity to share some knowledge and it's always good to go back and think and analyze why do we have a project right we create stuff we create projects but it's always good to understand why do we have this what type of problem we are trying to solve. And the biggest challenge today is that telemetry is everywhere, right? Every time we got more deployments, more services, more containers or or metal machines or embedded devices that chips even more telemetry, right? But as I said days before, nobody want to wake up in the morning and say, "Oh, I'm going to do observability." That's boring, right?

You want to do data analysis. Nobody want to manage the agents or taking care of this actually fluent bit is something that you run it and you would like to forget about it right um so telemetry data is everywhere and if data is everywhere means that it's in different places and different formats and if you want to do data analysis which is your final goal you need to have a way to move this data and centralizes centralize it in a place for data analysis right like a database splank elastic Open search or any solution that is available from a cloud provider. And where fluent bit sits, it's in the middle. And fluent bit basically is like what we call a telemetry pipeline. Right? The moment that you start understanding the lower concept, the best you can have a better implementation. And a telemetry pipeline pretty much has inputs where data collection happens. You have processors which allows you to modify the data that is being collected. Then you have a routing phase that says hey where this data will go and then you have the outputs which are pretty much connectors for backends like databases or cloud services.

Example of inputs for example tail read log files sys log receive data from open telemetry applications. We can do promeus scraping. We can collect kubernetes events. So it's not just to receive over the network but also from the local system even systemd if you want to pr
