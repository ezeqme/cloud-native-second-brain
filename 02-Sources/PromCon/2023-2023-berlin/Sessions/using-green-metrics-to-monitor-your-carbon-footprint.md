---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/using-green-metrics-to-monitor-your-carbon-footprint/
youtube_url: https://www.youtube.com/watch?v=LO9UyTKnIzc
youtube_search_url: https://www.youtube.com/results?search_query=Using+Green+Metrics+to+Monitor+your+Carbon+Footprint+PromCon+2023
video_match_score: 1.019
status: video-found
---

# Using Green Metrics to Monitor your Carbon Footprint

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/using-green-metrics-to-monitor-your-carbon-footprint/
- YouTube: https://www.youtube.com/watch?v=LO9UyTKnIzc

## Resumo

Speaker(s): Ida Fürjesová & Niki Manoledaki Carbon emissions from cloud computing are estimated to be more than the emissions from aviation. In this talk we will show you how to take a bottom-up approach to monitoring energy consumption and carbon emissions at a granular level when deploying cloud-native software and provisioning infrastructure. In order to reduce the carbon footprint of our infrastructure and software, the first step is to measure the energy consumption and carbon intensity of the applications we run and the tools we build.

## Abstract oficial

Speaker(s): Ida Fürjesová & Niki Manoledaki

Carbon emissions from cloud computing are estimated to be more than the emissions from aviation. In this talk we will show you how to take a bottom-up approach to monitoring energy consumption and carbon emissions at a granular level when deploying cloud-native software and provisioning infrastructure.

In order to reduce the carbon footprint of our infrastructure and software, the first step is to measure the energy consumption and carbon intensity of the applications we run and the tools we build. In this talk, we want to empower engineers to take control of the environments they are working in by setting up easy monitoring flows for gathering green metrics. Kepler, an eBPF energy monitoring tool and CNCF sandbox project, can export green metrics to Prometheus. Those metrics can then be visualized in Grafana, which provides an out-of-the-box support for Prometheus. We will demonstrate how to write PromQL queries that use Kepler metrics to monitor the energy consumed by Pods in namespaces. We will also show you how to convert energy metrics into carbon emission metrics.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/using-green-metrics-to-monitor-your-carbon-footprint/
- YouTube: https://www.youtube.com/watch?v=LO9UyTKnIzc
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LO9UyTKnIzc
- YouTube title: PromCon 2023 - Using Green Metrics to Monitor your Carbon Footprint
- Match score: 1.019
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/using-green-metrics-to-monitor-your-carbon-footprint/LO9UyTKnIzc.txt
- Transcript chars: 20840
- Keywords: energy, carbon, actually, emissions, metrics, kepler, sustainability, scheduling, consumption, question, reduce, another, electricity, footprint, security, working, cluster, centers

### Resumo baseado na transcript

[Music] hello uh today we will be talking about using green metrics to monitor your infrastructure's carbon footprint so my name is AA um for the last two and a half years I've been working for grafana laps as a software engineer um my passions are promoting the gender diversity intake and I'm trying to be an advocate for that and hi I'm Nikki I'm also a software engineer at grafana I'm also a cncf uh environmental sustainability tag uh contributor co-chair of the green reviews working group um the

### Excerpt da transcript

[Music] hello uh today we will be talking about using green metrics to monitor your infrastructure's carbon footprint so my name is AA um for the last two and a half years I've been working for grafana laps as a software engineer um my passions are promoting the gender diversity intake and I'm trying to be an advocate for that and hi I'm Nikki I'm also a software engineer at grafana I'm also a cncf uh environmental sustainability tag uh contributor co-chair of the green reviews working group um the tag en has been in place since a bit over a year now and our focus is uh advocating for green it in the cloud native ecosystem so uh since Nikki joh grafana she has been a great Advocate and uh she she has been promoting the topics of green metrics and sustainability in cloud and she got us together with Leonor Sophia Adam and myself and other great folks that are not not on this slide to join a hakon project uh that was uh deploying Kepler um in our Dev cluster and that's how this talk came about so today we will be talking about environmental sustainability uh and cloud computing um we will be focusing not on actually how to reduce carbon emissions or we won't be giving advice but the first step to reduce your emission is actually know um how much you're emitting so on this picture from from a climatic you can see that the share of global CO2 emissions um for data centers are in the range between 2.5% and 3.5 7% which is of quite a big range U it's in front of Aviation shipping and Rise cultivation and other sectors for me what was the shocking thing on this picture is that data centers are actually emitting more CO2 than Aviation I think that's quite high and also the range is pretty big if you think about it as the um share of global CO2 emissions I think this this picture shows us that um there is still it's not easy to collect uh data on emissions um in the data centers and also that we don't know we don't have the information of actually how much we are emitting exactly so why do you implement green Ops for your company or your business um I think the term net zero become became a buzzword u by 2050 I actually didn't even know what it means I don't know if you do but it means actually 90% reducing your emissions and 10% neutralizing so it's a pretty big commitment I think that term was uh coined in the during the Paris agreement uh talks and um many even very known corporations are committing to Net Zero by 20 we have 50 which is actually a quite tough th
