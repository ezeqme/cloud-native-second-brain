---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Networking"
themes: ["Networking", "Storage Data", "Kubernetes Core"]
speakers: ["Thomas Phelan", "Thomas Golway", "HPE"]
sched_url: https://kccncna2021.sched.com/event/lV5v/using-kubernetes-with-data-processing-units-to-offload-infrastructure-thomas-phelan-thomas-golway-hpe
youtube_search_url: https://www.youtube.com/results?search_query=Using+Kubernetes+with+Data+Processing+Units+to+Offload+Infrastructure+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Using Kubernetes with Data Processing Units to Offload Infrastructure - Thomas Phelan & Thomas Golway, HPE

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Thomas Phelan, Thomas Golway, HPE
- Schedule: https://kccncna2021.sched.com/event/lV5v/using-kubernetes-with-data-processing-units-to-offload-infrastructure-thomas-phelan-thomas-golway-hpe
- Busca YouTube: https://www.youtube.com/results?search_query=Using+Kubernetes+with+Data+Processing+Units+to+Offload+Infrastructure+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Using Kubernetes with Data Processing Units to Offload Infrastructure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV5v/using-kubernetes-with-data-processing-units-to-offload-infrastructure-thomas-phelan-thomas-golway-hpe
- YouTube search: https://www.youtube.com/results?search_query=Using+Kubernetes+with+Data+Processing+Units+to+Offload+Infrastructure+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=U6nC6cq3sWE
- YouTube title: Using Kubernetes with Data Processing Units to Offload Infrastructure- Thomas Phelan & Thomas Golway
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/using-kubernetes-with-data-processing-units-to-offload-infrastructure/U6nC6cq3sWE.txt
- Transcript chars: 19234
- Keywords: application, infrastructure, workloads, support, capabilities, running, business, workload, processing, ecosystem, applications, common, offload, software, specific, network, functionality, hardware

### Resumo baseado na transcript

hello welcome to this next cubecon north america 2021 session my name is tom phelan and my co-presenter today is tom galway we are both from hewlett-packard enterprise and we'll be discussing the why and how of using kubernetes with data processing units to offload software infrastructure i make the usual disclaimer that this is a discussion of what is possible it does not imply a commitment from hpe on specific product feature delivery now before we can discuss the use of data processing units more commonly known as dpus network security data plane management and data encryption or decryption this shields the services from any vendor-specific details of the infrastructure implementation the control services are a set of common services used to manage the configuration and operation of the dpu itself and these are examples of services which can run on the dpu and surface functionality to the containerized workloads in this example we see that telemetry information aggregation and logging functionality can be implemented on the gpu perhaps using a common logging service such as prometheus the same

### Excerpt da transcript

hello welcome to this next cubecon north america 2021 session my name is tom phelan and my co-presenter today is tom galway we are both from hewlett-packard enterprise and we'll be discussing the why and how of using kubernetes with data processing units to offload software infrastructure i make the usual disclaimer that this is a discussion of what is possible it does not imply a commitment from hpe on specific product feature delivery now before we can discuss the use of data processing units more commonly known as dpus with kubernetes we need to understand why we want to use them to run containerized workloads in the first place for this let me turn it over to tom galway to tell us about some recent developments and foundational trends in it thanks tom as tom mentioned let's start with some foundational trends we are seeing across the it spectrum starting with the shift in thinking when creating or transforming business initiatives digital disruption and digital transformation have been topics for some time but we're seeing an acceleration of enterprises shifting their business innovation strategies to embrace the concept of being digitally aware enterprises are adopting the concept of a digital ecosystem where the automation of business processes may be disaggregated and extend beyond the enterprise into third parties including suppliers partners customers and competitors enterprises are designing individual business initiatives within the digital ecosystem to be organized into a collection of processes and data interacting with in a virtual infrastructure the expectation is that this virtual infrastructure is optimized for the business outcome and fully abstracted from the physical infrastructure as enterprises innovate on the business side we see data and application architectures are shifting towards a more disaggregated model offering greater agility and supporting elasticity this is substantially changing the way i t resources are consumed the number of sources where data is created and ingested into the application ecosystem is increasing for example the proliferation of iot with its unique data models and contextual significance at the same time the value and usage of data is also changing which not only shapes the service levels required but also influences the gravitational pull being exerted by various entities within the digital ecosystem this gravitational pull influences the how and where compute and data need to be processed despite the h
