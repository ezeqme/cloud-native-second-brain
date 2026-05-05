---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Storage"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Junbao Kan", "Alibaba"]
sched_url: https://kccncna2021.sched.com/event/lV2I/large-scale-practice-of-persistent-memory-in-alibaba-cloud-junbao-kan-alibaba
youtube_search_url: https://www.youtube.com/results?search_query=Large-Scale+Practice+of+Persistent+Memory+in+Alibaba+Cloud+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Large-Scale Practice of Persistent Memory in Alibaba Cloud - Junbao Kan, Alibaba

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Storage]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Junbao Kan, Alibaba
- Schedule: https://kccncna2021.sched.com/event/lV2I/large-scale-practice-of-persistent-memory-in-alibaba-cloud-junbao-kan-alibaba
- Busca YouTube: https://www.youtube.com/results?search_query=Large-Scale+Practice+of+Persistent+Memory+in+Alibaba+Cloud+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Large-Scale Practice of Persistent Memory in Alibaba Cloud.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV2I/large-scale-practice-of-persistent-memory-in-alibaba-cloud-junbao-kan-alibaba
- YouTube search: https://www.youtube.com/results?search_query=Large-Scale+Practice+of+Persistent+Memory+in+Alibaba+Cloud+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3MKbk7AS8Jw
- YouTube title: Large-Scale Practice of Persistent Memory in Alibaba Cloud - Junbao Kan & Qingcan Wang, Alibaba
- Match score: 0.864
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/large-scale-practice-of-persistent-memory-in-alibaba-cloud/3MKbk7AS8Jw.txt
- Transcript chars: 17007
- Keywords: memory, volume, capacity, resource, device, scheduling, policy, application, manager, introduce, resize, source, cluster, defines, result, automatic, plugin, radius

### Resumo baseado na transcript

hello everyone my name is from alibaba cloud today my colleague jimbo and i will give our talk about the large skill practice of persistent memory in alibaba cloud on kubernetes this is our profile you can contact us through github or email this is our this is the agenda of today's topic in the first part i will introduce the system architecture of pmm stack the second part we will introduce the practice of pmount stack used in our company and the third is the demo and the fourth

### Excerpt da transcript

hello everyone my name is from alibaba cloud today my colleague jimbo and i will give our talk about the large skill practice of persistent memory in alibaba cloud on kubernetes this is our profile you can contact us through github or email this is our this is the agenda of today's topic in the first part i will introduce the system architecture of pmm stack the second part we will introduce the practice of pmount stack used in our company and the third is the demo and the fourth is the other related works about pima so why is persistence memory presence memory is a higher performance by two addressable memory device being on the memory bus low emp memory has the memory the ram like access through data and persistence memory has a following filters the first one is data persistence and the second the the second is the higher performance and the light capacity and the low price and why we used the p memory p map in our company it is the first day's cache database is large capacity memory space and the second is large we want to save our cost and then let's see the necessary of using p mapping kubernetes pmap is typically used as field system volume 2 application which can be provided as a persistence volume with csi first containerized more application i containerized in currently many payload eye deployment on kubernetes platform and use the storage results as volumes so pmap used in container becomes more and more requirements secondly automatic kubernetes manage pmap device automatic with kubernetes customized controller pmap can be initialized as defined policy and also pmom device can be provided as namespace and a field system automatic thirdly pmap can provide more than tb capacity on onenote so resource sharing is necessary between different users so the resource limit is requirements in the production and then is capacity aware capacity on a single node is limited so we need to report resource capacity of the node to the scheduler scheduler will determine the location of the new port based on the capacity of the pmap in the entire cluster this is how this is the architecture of pmom stack that's the dark with the architecture diagram on the right as the bottom of the graph is node resource manager node resource manager is responsible for automatic initialized pmap device and it also formats the device and mounted as fuel system which can be used as directly by accessed by application and node resource manager is deployed as demo set and works on ea
