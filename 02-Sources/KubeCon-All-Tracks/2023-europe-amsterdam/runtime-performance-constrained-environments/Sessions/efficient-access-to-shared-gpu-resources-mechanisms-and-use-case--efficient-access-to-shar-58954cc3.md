---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Runtime Performance + Constrained Environments"
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: ["Diogo Filipe Tomas Guerra", "Diana Gaponcic", "CERN"]
sched_url: https://kccnceu2023.sched.com/event/1HybB/efficient-access-to-shared-gpu-resources-mechanisms-and-use-cases-diogo-filipe-tomas-guerra-diana-gaponcic-cern
youtube_search_url: https://www.youtube.com/results?search_query=Efficient+Access+to+Shared+GPU+Resources%3A+Mechanisms+and+Use+Cases+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Efficient Access to Shared GPU Resources: Mechanisms and Use Cases - Diogo Filipe Tomas Guerra & Diana Gaponcic, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Runtime Performance + Constrained Environments]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Diogo Filipe Tomas Guerra, Diana Gaponcic, CERN
- Schedule: https://kccnceu2023.sched.com/event/1HybB/efficient-access-to-shared-gpu-resources-mechanisms-and-use-cases-diogo-filipe-tomas-guerra-diana-gaponcic-cern
- Busca YouTube: https://www.youtube.com/results?search_query=Efficient+Access+to+Shared+GPU+Resources%3A+Mechanisms+and+Use+Cases+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Efficient Access to Shared GPU Resources: Mechanisms and Use Cases.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HybB/efficient-access-to-shared-gpu-resources-mechanisms-and-use-cases-diogo-filipe-tomas-guerra-diana-gaponcic-cern
- YouTube search: https://www.youtube.com/results?search_query=Efficient+Access+to+Shared+GPU+Resources%3A+Mechanisms+and+Use+Cases+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jkcEQE9C338
- YouTube title: Efficient Access to Shared GPU Resources: Mechanisms and Use Cases - Diogo Guerra & Diana Gaponcic
- Match score: 0.903
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/efficient-access-to-shared-gpu-resources-mechanisms-and-use-cases/jkcEQE9C338.txt
- Transcript chars: 25586
- Keywords: gpu, actually, memory, basically, slicing, resources, orange, utilization, better, compute, benchmarking, resource, question, nvidia, operator, everything, thanks, shared

### Resumo baseado na transcript

thank you for attending our session we were not sure we're gonna receive thank you for attending our session we were not sure we're gonna receive such a big interest in our topic but we're very happy to see you and let's start so this is a GPU talk too many users very little resources thank you for coming we're presenting efficient access to share GPU resources with a Computing engineer with the CERN kubernetes team I'm Diana I'm a Computing engineer as at CERN as well okay so for

### Excerpt da transcript

thank you for attending our session we were not sure we're gonna receive thank you for attending our session we were not sure we're gonna receive such a big interest in our topic but we're very happy to see you and let's start so this is a GPU talk too many users very little resources thank you for coming we're presenting efficient access to share GPU resources with a Computing engineer with the CERN kubernetes team I'm Diana I'm a Computing engineer as at CERN as well okay so for a bit of context certain is the European Center for nuclear research the largest particle physics laboratory in the world situated in Geneva Switzerland we one of our biggest apparatus is a circular accelerator which accelerates protons close to the speed of light and clockwise and anti-clockwise and in certain points of this accelerator we make them collide this is one of these points is the compact muon solenoid which is not very Compact and uh and basically it acts like a big photographic camera which takes uh 40 million pictures per second this is one example of one of those pictures and each accelerator it's a detector can produce about terabytes of data a second so we actually filtered this data with hardware and software um filtering and to make it down to a more manageable size of on the order of 10 gigabits a second but still with all the all the detectors before we generate about 70 petabytes of data a year and this is just only going to grow up so we have a very big and large data set and but the good thing is that this is highly parallelizable which is great for gpus and also in the community we use the gpus to do simulation even filtering as I explained and also some other event reconstruction or anal physics um data to process the data um so we have some challenges when using CPU gpus um some of them some users have sub-optimal code um basically because they have some strong interactions between CPU GPU or they move memory around other types of challenges these Legacy code which we do have a lot and basically code was not designed for CPUs and the people just bought them to gpus it's not going to work the same way and also some workloads which are spiking nature so for example we can take this as a as a scientist developing some algorithm on the notebooks and basically it's just seat idle and it doesn't use the GPU at all on the other hand there's some infrastructure perspective about the GPU power density constraints but probably the most important is the limited r
