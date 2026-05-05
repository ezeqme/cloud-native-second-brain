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
themes: ["AI ML", "Platform Engineering", "SRE Reliability"]
speakers: ["Zoram Thanga", "Peter Ableda", "Cloudera"]
sched_url: https://kccncna2024.sched.com/event/1i7mR/production-ai-at-scale-clouderas-journey-in-building-a-robust-inference-platform-zoram-thanga-peter-ableda-cloudera
youtube_search_url: https://www.youtube.com/results?search_query=Production+AI+at+Scale%3A+Cloudera%E2%80%99s+Journey+in+Building+a+Robust+Inference+Platform+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Production AI at Scale: Cloudera’s Journey in Building a Robust Inference Platform - Zoram Thanga & Peter Ableda, Cloudera

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Zoram Thanga, Peter Ableda, Cloudera
- Schedule: https://kccncna2024.sched.com/event/1i7mR/production-ai-at-scale-clouderas-journey-in-building-a-robust-inference-platform-zoram-thanga-peter-ableda-cloudera
- Busca YouTube: https://www.youtube.com/results?search_query=Production+AI+at+Scale%3A+Cloudera%E2%80%99s+Journey+in+Building+a+Robust+Inference+Platform+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Production AI at Scale: Cloudera’s Journey in Building a Robust Inference Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7mR/production-ai-at-scale-clouderas-journey-in-building-a-robust-inference-platform-zoram-thanga-peter-ableda-cloudera
- YouTube search: https://www.youtube.com/results?search_query=Production+AI+at+Scale%3A+Cloudera%E2%80%99s+Journey+in+Building+a+Robust+Inference+Platform+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VnTHlo56AI4
- YouTube title: Production AI at Scale: Cloudera’s Journey in Building a Robust Inference Pl... Z. Thanga, P. Ableda
- Match score: 0.952
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/production-ai-at-scale-clouderas-journey-in-building-a-robust-inferenc/VnTHlo56AI4.txt
- Transcript chars: 27676
- Keywords: models, inference, support, running, ranger, registry, security, requirements, source, basically, platform, workbench, customers, access, control, server, production, enterprise

### Resumo baseado na transcript

thank you everyone for attending this session on us explaining you know how um Cloudera build uh really scalable and robust AI inferencing platform we're glad that you can make it and um hopefully uh you take away uh some tidbits of information uh that can help you in your own Journeys so my name is sang I'm a principal engineer at uh Cloud hi my name is Peter uh I'm a director of product management uh working on Enterprise Solutions and I'm going to kick us off uh I

### Excerpt da transcript

thank you everyone for attending this session on us explaining you know how um Cloudera build uh really scalable and robust AI inferencing platform we're glad that you can make it and um hopefully uh you take away uh some tidbits of information uh that can help you in your own Journeys so my name is sang I'm a principal engineer at uh Cloud hi my name is Peter uh I'm a director of product management uh working on Enterprise Solutions and I'm going to kick us off uh I will start with some historical context uh Cloud era caters for the entire data science machine learning and AI life cycle and this is the this is these are capabilities that we had uh even last year how we Define the life cycle is it always starts with data engine pipelines uh you need to have data uh present in your systems to drive your AI use cases once you have the data uh data scientists typically do uh exploratory data science they work on understanding the data they have at hand um they uh look at the characteristics shapes and size of the data once they have a good understanding they can actually build a machine learning model uh they can train a traditional model they can fune a model or they can do some promt engineering once they have a model ready uh they need to package it uh Reg register it into a a model registry for long-term cataloging and once in the registry they can deploy to a serving environment uh where uh they can uh serve the incoming um mod requests and then uh once something is running in production they need to make sure that it's up and running and healthy so they need to monitor everything under under the hood they to make sure that it's it's up to par and at the last stage they need to build an AI application data scientists don't build data science models just for the sake of it there is always one specific business problem one specific use case that they are looking to solve and that's typically complete by building an application and the application is a is a pretty vake concept uh it can mean anything it can be a web application that they host for business stakeholders it can be a weekly report that they send out it can be a mobile application that integrates with the rest end point the point here is that you need an application to complete your use case for the longest time Cloud era had the cloud AI workbench as the the solution for this endtoend life cycle uh and in the next couple of slides I'm going to go into detail what are the actual requirements for
