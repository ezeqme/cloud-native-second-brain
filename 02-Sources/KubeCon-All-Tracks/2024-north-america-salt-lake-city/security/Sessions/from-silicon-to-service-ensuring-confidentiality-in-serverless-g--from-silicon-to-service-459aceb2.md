---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["Zvonko Kaiser", "NVIDIA"]
sched_url: https://kccncna2024.sched.com/event/1i7nF/from-silicon-to-service-ensuring-confidentiality-in-serverless-gpu-cloud-functions-zvonko-kaiser-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=From+Silicon+to+Service%3A+Ensuring+Confidentiality+in+Serverless+GPU+Cloud+Functions+CNCF+KubeCon+2024
slides: []
status: parsed
---

# From Silicon to Service: Ensuring Confidentiality in Serverless GPU Cloud Functions - Zvonko Kaiser, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Salt Lake City
- Speakers: Zvonko Kaiser, NVIDIA
- Schedule: https://kccncna2024.sched.com/event/1i7nF/from-silicon-to-service-ensuring-confidentiality-in-serverless-gpu-cloud-functions-zvonko-kaiser-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=From+Silicon+to+Service%3A+Ensuring+Confidentiality+in+Serverless+GPU+Cloud+Functions+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre From Silicon to Service: Ensuring Confidentiality in Serverless GPU Cloud Functions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nF/from-silicon-to-service-ensuring-confidentiality-in-serverless-gpu-cloud-functions-zvonko-kaiser-nvidia
- YouTube search: https://www.youtube.com/results?search_query=From+Silicon+to+Service%3A+Ensuring+Confidentiality+in+Serverless+GPU+Cloud+Functions+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nkZdNRXm3jY
- YouTube title: From Silicon to Service: Ensuring Confidentiality in Serverless GPU Cloud Functions - Zvonko Kaiser
- Match score: 1.001
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/from-silicon-to-service-ensuring-confidentiality-in-serverless-gpu-clo/nkZdNRXm3jY.txt
- Transcript chars: 29257
- Keywords: running, confidential, container, kernel, attestation, operating, containers, essentially, runtime, cannot, working, protect, attest, coming, hardware, hypervisor, against, measurements

### Resumo baseado na transcript

thanks everyone for coming uh my name is wano Kaiser I'm with Nvidia in the cloud native team um my main responsibilities are kada and confidential containers and today I want to talk about a topic from Silicon to service the full stack ensuring confidentiality in sess GPU clo functions so who has been in uh cucon EU in Paris may have seen my talk on confident confidential containers with GPU and Rec LMS so just recap what we've done in the space right uh I talked about the road

### Excerpt da transcript

thanks everyone for coming uh my name is wano Kaiser I'm with Nvidia in the cloud native team um my main responsibilities are kada and confidential containers and today I want to talk about a topic from Silicon to service the full stack ensuring confidentiality in sess GPU clo functions so who has been in uh cucon EU in Paris may have seen my talk on confident confidential containers with GPU and Rec LMS so just recap what we've done in the space right uh I talked about the road to confidential Computing what we've done in the space uh why we've chosen Kata for for implementing confidential compute with the gpus on kubernetes uh explained a little bit about the GPU enablement stack uh the virualization reference architecture uh what we need to take care about um to enable Advanced use cases like GPU direct RDMA or GDs uh how we implemented confidential containers and then as an example uh how we can run regular lamps with confidential containers um I link the recording so if everybody interested on the lowlevel details what I've done in this space uh go check it out um today I want to expand on the use cases that we are doing with confidential containers and uh role of the working groups that we established in the Upstream community so one of the working groups is our confidential containers use case working group um different companies from IBM M redhead uh Nvidia uh Intel IMD are involved in all of this and we identified three major use cases that we want to enable and push forward Upstream uh number one is Federated learning uh which includes um a data clean room so we have different peers and integration server working in one confidential environment so we need to share this environment and provide a data clean room for multiple personas uh which also ties into multi party Computing right it's not only a single note where we running a confidential container it's multiple notes and we need to take care care of that um the other big topic is of course if you're running a confidential environment everything needs to be trusted be it your build pipeline your cicd pipeline so we have several members of our community they are working on the supply chain security right uh all things related to as bombs Provence uh cicd and repeatability of of builds and attestation of builds and deliverables that we are having in the Enclave or a confidential envirment uh and of course generative AI Rec llms nyss um how to properly deploy them how to properly secure them um s
