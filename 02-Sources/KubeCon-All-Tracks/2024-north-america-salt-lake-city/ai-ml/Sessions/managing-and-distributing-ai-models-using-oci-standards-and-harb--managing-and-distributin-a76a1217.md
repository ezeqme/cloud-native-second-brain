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
themes: ["AI ML"]
speakers: ["Steven Zou", "VMware by Broadcom"]
sched_url: https://kccncna2024.sched.com/event/1i7pB/managing-and-distributing-ai-models-using-oci-standards-and-harbor-steven-zou-vmware-by-broadcom
youtube_search_url: https://www.youtube.com/results?search_query=Managing+and+Distributing+AI+Models+Using+OCI+Standards+and+Harbor+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Managing and Distributing AI Models Using OCI Standards and Harbor - Steven Zou, VMware by Broadcom

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Steven Zou, VMware by Broadcom
- Schedule: https://kccncna2024.sched.com/event/1i7pB/managing-and-distributing-ai-models-using-oci-standards-and-harbor-steven-zou-vmware-by-broadcom
- Busca YouTube: https://www.youtube.com/results?search_query=Managing+and+Distributing+AI+Models+Using+OCI+Standards+and+Harbor+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Managing and Distributing AI Models Using OCI Standards and Harbor.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pB/managing-and-distributing-ai-models-using-oci-standards-and-harbor-steven-zou-vmware-by-broadcom
- YouTube search: https://www.youtube.com/results?search_query=Managing+and+Distributing+AI+Models+Using+OCI+Standards+and+Harbor+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0eiXSogHxmQ
- YouTube title: Managing and Distributing AI Models Using OCI Standards and Harbor - Steven Zou
- Match score: 1.003
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/managing-and-distributing-ai-models-using-oci-standards-and-harbor/0eiXSogHxmQ.txt
- Transcript chars: 23599
- Keywords: harbor, registry, models, container, artifact, artifacts, version, support, replication, create, access, already, management, actually, specific, managing, another, standard

### Resumo baseado na transcript

uh hello everyone uh good afternoon and uh thanks for coming to this session uh managing and distributing uh AI models using OC centers and harbor uh I'm Steven zo I'm a software engineer from VMware bom I'm also a maintainer of Harbor project and we have a cool speaker because some reason he cannot come here so today only me uh to deliver this uh session uh to move to next slide I'd like to do a very quick survey uh how many uh of you are here are

### Excerpt da transcript

uh hello everyone uh good afternoon and uh thanks for coming to this session uh managing and distributing uh AI models using OC centers and harbor uh I'm Steven zo I'm a software engineer from VMware bom I'm also a maintainer of Harbor project and we have a cool speaker because some reason he cannot come here so today only me uh to deliver this uh session uh to move to next slide I'd like to do a very quick survey uh how many uh of you are here are working on AI related fields you can oh cool quite a lot uh yeah hopefully we can get more feedback from you and uh another how many of you are here today are familiar with haror oh cool oh cool I think is so many hper fans okay uh the topic of this uh of this talk is in word it's um uh Harbor can be used as a not only as a container registry to support uh uh deploying container r workloads on kubernetes it can also serve as a fully featured model registry to support AI workflows on kuber Naes here is the agenda for today's paration first I'll briefly discuss the motivations behind this idea and then I'll uh uh cover some background focus on the what's o and the what har can do uh next I introduce the overall idea of model registry after that we'll go through how this idea can be imp implemented in within Harbor uh following that uh I present to end demo uh at streat the a model scenario uh finally we'll uh wrap up with uh discussion on partial future directions okay uh kubernetes yeah has involved over the last 10 years into the defao platform for ation uh containerized workloads with container registry as a back ball uh for managing these flows uh with AI on the r uh kubernetes is uh increasing uh the platform of choice for AI uh workloads like trainers and a driving applications so these workf flows require not only uh code but also models and data side at call assets so the question is how can we um manage these AI assets uh within the kubernetes ecosystem rusing existing proven uh tools the community is uh already take Taking actions Comm 1.31 now supports also compatible artifact as image volumes uh providing a way to integrate more models uh and the data size and O artifacts uh in can registry um extending container registry uh to AI model registry that FS similarly uh into Community will bring uh obers uh benefits many organization already run kubernetes uh and O compatible reg so using ocf for model means the same ecosystem can handle AI work workloads alongside traditional applications uh this compatib
