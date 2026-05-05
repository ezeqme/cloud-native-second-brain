---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["AI ML"]
speakers: ["Sampath Priyankara", "Nippon Telegraph and Telephone Corporation", "Masataka Sonoda", "Fujitsu Limited"]
sched_url: https://kccnceu2024.sched.com/event/1YeMR/acceleratorsfpgagpu-chaining-to-efficiently-handle-large-aiml-workloads-in-k8s-sampath-priyankara-nippon-telegraph-and-telephone-corporation-masataka-sonoda-fujitsu-limited
youtube_search_url: https://www.youtube.com/results?search_query=Accelerators%28FPGA%2FGPU%29+Chaining+to+Efficiently+Handle+Large+AI%2FML+Workloads+in+K8s+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Accelerators(FPGA/GPU) Chaining to Efficiently Handle Large AI/ML Workloads in K8s - Sampath Priyankara, Nippon Telegraph and Telephone Corporation & Masataka Sonoda, Fujitsu Limited

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]]
- País/cidade: France / Paris
- Speakers: Sampath Priyankara, Nippon Telegraph and Telephone Corporation, Masataka Sonoda, Fujitsu Limited
- Schedule: https://kccnceu2024.sched.com/event/1YeMR/acceleratorsfpgagpu-chaining-to-efficiently-handle-large-aiml-workloads-in-k8s-sampath-priyankara-nippon-telegraph-and-telephone-corporation-masataka-sonoda-fujitsu-limited
- Busca YouTube: https://www.youtube.com/results?search_query=Accelerators%28FPGA%2FGPU%29+Chaining+to+Efficiently+Handle+Large+AI%2FML+Workloads+in+K8s+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Accelerators(FPGA/GPU) Chaining to Efficiently Handle Large AI/ML Workloads in K8s.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeMR/acceleratorsfpgagpu-chaining-to-efficiently-handle-large-aiml-workloads-in-k8s-sampath-priyankara-nippon-telegraph-and-telephone-corporation-masataka-sonoda-fujitsu-limited
- YouTube search: https://www.youtube.com/results?search_query=Accelerators%28FPGA%2FGPU%29+Chaining+to+Efficiently+Handle+Large+AI%2FML+Workloads+in+K8s+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aDVPTQ7idhM
- YouTube title: Accelerators(FPGA/GPU) Chaining to Efficiently Handle Large AI/ML Workloads in K8s
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/accelerators-fpga-gpu-chaining-to-efficiently-handle-large-ai-ml-workl/aDVPTQ7idhM.txt
- Transcript chars: 25180
- Keywords: function, connection, functions, operators, accelerators, resources, processing, process, gpu, workloads, resource, operator, pipeline, inference, network, define, change, individual

### Resumo baseado na transcript

good evening everyone uh thank you for joining us today my name is Sak from NTT and my colleague here masataka from Fujitsu so we are here to talk about uh acceleration chaining to efficiently handle large AIML workloads in kubernetes so uh please allow me to begin this speak so uh in this talk first uh I would like to give you introduction to our work and then discuss about what are the large workloads we are mentioned here and then uh I will give you a brief introduction

### Excerpt da transcript

good evening everyone uh thank you for joining us today my name is Sak from NTT and my colleague here masataka from Fujitsu so we are here to talk about uh acceleration chaining to efficiently handle large AIML workloads in kubernetes so uh please allow me to begin this speak so uh in this talk first uh I would like to give you introduction to our work and then discuss about what are the large workloads we are mentioned here and then uh I will give you a brief introduction to the acceleration method currently we use in the the kubernetes and advanced setups to how to accelerate the processes and then uh I will jump into the challenges of the the process acceleration in current kubernetes and then we will present uh the our uh kubernetes extensions for efficiently handle the accelerations and the the communication between the accelerators and uh before we wrap up the presentation uh I would like we would like to give you uh the live demonstration I don't know how far we can go with the live but I'll give you this demonstration and I have the video for the backup purposes so finally uh I hope to wrap up the presentation with our future works so uh in kubernetes recently uh especially in this uh 3 four years the with the WID spread adaption of the AI and ml uh uh the application and the the methods the development Frameworks backed by the kubernetes is have become increasingly utilized so I try to uh put up some of the projects which use kubernetes in the AI and ml uh the ecosystem so uh I only managed to list a few of them but uh as you may know there's a huge amount of project in cncf which involving with the the AI and ml the development and the application serving process so so uh the normally uh in generally this uh these Frameworks use kubernetes as orchestrator for the resource management so uh normally this uh the the pipelines or the so-called the workflows is defined uh in a we can Define it in the scripts or the UI and then it's come to the the tool kit or the the uh the the tooling section and then we Define the pipe lines uh as like a chain of process like uh and uh this concept is coming from the the the chaining the processes in the single pipeline so in the pipeline we can uh pipeline is consist with the the smallest atomic parts called steps so the terminology might be different from the whatever tool you use but the the basic idea is the pipeline and it's it made by this the single steps so uh once you uh once you ask kubernetes to allocate
