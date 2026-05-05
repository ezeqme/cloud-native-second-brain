---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["AI ML", "Storage Data"]
speakers: ["Shawn Sun", "Lu Qiu", "Alluxio"]
sched_url: https://kccncna2023.sched.com/event/1R2vs/the-journey-along-the-way-to-data-locality-on-cloud-for-aiml-shawn-sun-lu-qiu-alluxio
youtube_search_url: https://www.youtube.com/results?search_query=The+Journey+Along+the+Way+to+Data-locality+on+Cloud+for+AI%2FML+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The Journey Along the Way to Data-locality on Cloud for AI/ML - Shawn Sun & Lu Qiu, Alluxio

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: United States / Chicago
- Speakers: Shawn Sun, Lu Qiu, Alluxio
- Schedule: https://kccncna2023.sched.com/event/1R2vs/the-journey-along-the-way-to-data-locality-on-cloud-for-aiml-shawn-sun-lu-qiu-alluxio
- Busca YouTube: https://www.youtube.com/results?search_query=The+Journey+Along+the+Way+to+Data-locality+on+Cloud+for+AI%2FML+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The Journey Along the Way to Data-locality on Cloud for AI/ML.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vs/the-journey-along-the-way-to-data-locality-on-cloud-for-aiml-shawn-sun-lu-qiu-alluxio
- YouTube search: https://www.youtube.com/results?search_query=The+Journey+Along+the+Way+to+Data-locality+on+Cloud+for+AI%2FML+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RD_SMOrFLJU
- YouTube title: The Journey Along the Way to Data-locality on Cloud for AI/ML - Shawn Sun & Lu Qiu, Alluxio
- Match score: 0.91
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-journey-along-the-way-to-data-locality-on-cloud-for-ai-ml/RD_SMOrFLJU.txt
- Transcript chars: 20358
- Keywords: training, storage, actually, performance, cost, remote, chaining, worker, inference, basically, higher, solution, machine, learning, second, especially, management, locality

### Resumo baseado na transcript

so today we will be sharing our journey along the the way to data locality on Cloud for machine learning and AI workloads my name is Sean I'm a software engineer at loil and my colleague Lou Who will be talking about the second half of the deck later she's a machine learning engineer at Lille and the same time she's also PMT member of our Alexa open source project so here's agenda of today so first we'll talk about the benefits of data locality and what are some of

### Excerpt da transcript

so today we will be sharing our journey along the the way to data locality on Cloud for machine learning and AI workloads my name is Sean I'm a software engineer at loil and my colleague Lou Who will be talking about the second half of the deck later she's a machine learning engineer at Lille and the same time she's also PMT member of our Alexa open source project so here's agenda of today so first we'll talk about the benefits of data locality and what are some of the existing Solutions then we'll bring up a new design along with this implementation and finally about some production use case and the integration between lox and AR aray so first about the advantages of bring data locality to Cloud there are two main reasons the first is performance game compared to remote storage like S3 or AER or gcp you have faster access to the data therefore there will be less time spent on data intensive applications especially machine learning and AI over clads the second main reason is about cost cost saving because by reading from us there will be fewer API costs made to the cloud storage this includes both St data and metadata API cost and because of the performance gain we have higher utilization of your GPU less tribute time Le also leads to less cost now we'll look at some of the existing Solutions out there there are the main mainstream has like two or four Solutions first is to read data directly from remote storage on fly second is to copy data from remote to local before the training the third is to use a local cach layer for data reuse and lastly we can use a distributed cache system let's go over the one by one so first if we always read from read data from remote storage there will be no data locality this is the easiest way to sell up but at the same time every app training needs to reread all the data from remote and because multiple AO are always always needed for better accuracy I mean there's no way your training only involved one Appo and then reading from remote will take can take more time than the actual training so here's a screenshot that we uh did a test this is a uh P torch training on a subet of image net so you can see 82% per of the time is actually spent by the data loader instead of the ACT actual training oh by the way the uh this tested data was on on S3 so the second way we just mention is to copy the data to local before training so now the data is local so that so that you can get all the benefits of data locality that incl Bo cost
