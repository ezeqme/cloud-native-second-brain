---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Serverless"
themes: ["SRE Reliability"]
speakers: ["Cathy Zhang", "Rui Zang", "Intel"]
sched_url: https://kccnceu2022.sched.com/event/ytmx/crack-the-faas-cold-start-and-scalability-bottleneck-cathy-zhang-rui-zang-intel
youtube_search_url: https://www.youtube.com/results?search_query=Crack+the+FaaS+Cold+Start+and+Scalability+Bottleneck+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Crack the FaaS Cold Start and Scalability Bottleneck - Cathy Zhang & Rui Zang, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Serverless]]
- Temas: [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Cathy Zhang, Rui Zang, Intel
- Schedule: https://kccnceu2022.sched.com/event/ytmx/crack-the-faas-cold-start-and-scalability-bottleneck-cathy-zhang-rui-zang-intel
- Busca YouTube: https://www.youtube.com/results?search_query=Crack+the+FaaS+Cold+Start+and+Scalability+Bottleneck+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Crack the FaaS Cold Start and Scalability Bottleneck.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytmx/crack-the-faas-cold-start-and-scalability-bottleneck-cathy-zhang-rui-zang-intel
- YouTube search: https://www.youtube.com/results?search_query=Crack+the+FaaS+Cold+Start+and+Scalability+Bottleneck+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RUfcc-OpBAM
- YouTube title: Crack the FaaS Cold Start and Scalability Bottleneck - Cathy Zhang & Rui Zang, Intel
- Match score: 0.874
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/crack-the-faas-cold-start-and-scalability-bottleneck/RUfcc-OpBAM.txt
- Transcript chars: 15898
- Keywords: function, snapshot, instance, blocks, latency, essential, creating, unique, existing, starting, platform, container, process, approach, instances, execution, running, specific

### Resumo baseado na transcript

hello everyone welcome to our session on crack the fast cold start and the scalability bottleneck my name is kaiser zhang along with me is ree zhang we both work in the cloud native area at intel's central software engineering team and here's what we will cover in today's presentation first we will give a brief overview on the first and the major challenges faced by current fast providers then we will go through the steps involved in a fast function called start process and analyze which steps contribute the

### Excerpt da transcript

hello everyone welcome to our session on crack the fast cold start and the scalability bottleneck my name is kaiser zhang along with me is ree zhang we both work in the cloud native area at intel's central software engineering team and here's what we will cover in today's presentation first we will give a brief overview on the first and the major challenges faced by current fast providers then we will go through the steps involved in a fast function called start process and analyze which steps contribute the most to the code start latency after that we will deep dive into a new approach of creating a function instance from a snapshot we will also talk a little bit about the auto scaling bottleneck and our approach of scanning out new function instances inside of existing microvia last we will show our test result and compare the code start latency between existing way of starting a function instance versus our snapshot based way of starting a function instance um before i deep dive into a snapshot based way of starting a function instance i would like to first set up the context for the discussion so what is fast fast is an event driven architecture-based computing service which allocates micro vms or containers on the mount to run the developer's function code in response to event requests fast provides three key features the first feature is automatic on-demand instantiation of function instances to run the function code upon a trigger event the second feature is on demand auto scaling out and in no need for the user to plan for peak traffic and the third feature is utility based bidding the user never pays for idle time and fun okay sorry it's code too much um fast is said to be the future of cloud computing it is gaining a lot of momentum in the industry the diagrams on the right are sourced from data doc the top diagram shows the percentage of organizations using fuss provided by aws on seo and google cloud at least one in five organizations is adopting fast and the bottom diagram shows the average daily invocations plan the function index from 2019 to 2021 the lambda functions are evoked 3.5 times more often in 2021 than in 2019 and to support multi-tenancy and security functions are usually run inside a micro vm like sandbox advance provides a lot of benefits to the user for example the users do not need to manage any infrastructure since the first platform will take care of when and how to create a function micro vm the fast platform will manage au
