---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML", "Observability", "Kubernetes Core", "SRE Reliability"]
speakers: ["Ashok Chandrasekar", "Google", "Liudmila Molkova", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1i7lA/optimizing-llm-performance-in-kubernetes-with-opentelemetry-ashok-chandrasekar-google-liudmila-molkova-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Optimizing+LLM+Performance+in+Kubernetes+with+OpenTelemetry+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Optimizing LLM Performance in Kubernetes with OpenTelemetry - Ashok Chandrasekar, Google & Liudmila Molkova, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Observability]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Ashok Chandrasekar, Google, Liudmila Molkova, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1i7lA/optimizing-llm-performance-in-kubernetes-with-opentelemetry-ashok-chandrasekar-google-liudmila-molkova-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Optimizing+LLM+Performance+in+Kubernetes+with+OpenTelemetry+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Optimizing LLM Performance in Kubernetes with OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lA/optimizing-llm-performance-in-kubernetes-with-opentelemetry-ashok-chandrasekar-google-liudmila-molkova-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Optimizing+LLM+Performance+in+Kubernetes+with+OpenTelemetry+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6rdeFACyyYg
- YouTube title: Optimizing LLM Performance in Kubernetes with OpenTelemetry - Ashok Chandrasekar & Liudmila Molkova
- Match score: 0.846
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/optimizing-llm-performance-in-kubernetes-with-opentelemetry/6rdeFACyyYg.txt
- Transcript chars: 28128
- Keywords: latency, scaling, seconds, server, metrics, request, tokens, throughput, actually, performance, client, context, second, utilization, workloads, metric, around, requests

### Resumo baseado na transcript

what are we going to talk about about uh optimizing kolam performance uh with open Telemetry uh let us introduce ourselves hi I'm mashuk Chandra I'm a senior software engineer at Google I work on a inference uh workloads performance optimization and I'm also leading the benchmarking and Metric standardization effort in cative serving working group and I'm Luda mova I work on up and Telemetry and uh on Azure client libraries I'm technical Committee Member and a maintainer of open Telemetry semantic conventions so we are going to start

### Excerpt da transcript

what are we going to talk about about uh optimizing kolam performance uh with open Telemetry uh let us introduce ourselves hi I'm mashuk Chandra I'm a senior software engineer at Google I work on a inference uh workloads performance optimization and I'm also leading the benchmarking and Metric standardization effort in cative serving working group and I'm Luda mova I work on up and Telemetry and uh on Azure client libraries I'm technical Committee Member and a maintainer of open Telemetry semantic conventions so we are going to start with a quick intro uh what's special about uh LM gen you call it uh we will talk about the observability needs of uh gen applications and workloads uh we will quickly dive into client side of the Telemetry things and then a sh will take cover and talk about uh the model server site we will do a quick demo and uh talk more about a scaling and the server side of things finally we hope we can influence you to come contribute to some of the things we're working on if you're interested and we are going to share how you can participate okay so um llms are getting more popular uh but also self hosting LMS is getting very popular um for example hugging phase has more than a million models hosted now and a very active community of people um kubernetes be is becoming a preferred platform to host this workloads and there are new capabilities uh being introduced for uh specifically for a Amal workloads um okay so in terms of performance and observability what's special right so first it's it's a new technology is growing really fast uh there are a lot of new usage patterns uh they have kind of high complexity right uh the uh responses are not deterministic we now need to evaluate them we need to record this Telemetry in a certain way um and also on the server side the operations are kind of different than when you serve the HTTP apis and we need different insights into this very computer and data intensive uh workloads and to be fair we just don't know how to use the thing right we as an industry we are all trying to figure out how to use llms and what does it mean to for it to be optimal um then how um how to get insights into it um yeah okay so let's dive into the client side first um so on the client side uh as a member of open Telemetry I'm going to talk about up Telemetry we are working actively on uh defining semantic conventions and building instrumentation libraries let me quickly uh share what it means so um we want people to use
