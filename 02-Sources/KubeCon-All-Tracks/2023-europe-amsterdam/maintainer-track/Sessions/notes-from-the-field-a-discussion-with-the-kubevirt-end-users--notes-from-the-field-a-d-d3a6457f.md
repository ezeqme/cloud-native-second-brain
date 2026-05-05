---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Alona Paz", "Red Hat", "Ryan Hallisey", "Nvidia", "Dinesh Majrekar", "Civo", "Kim Wüstkamp", "Killercoda", "Peter Salanki", "CoreWeave"]
sched_url: https://kccnceu2023.sched.com/event/1HyRz/notes-from-the-field-a-discussion-with-the-kubevirt-end-users-alona-paz-red-hat-ryan-hallisey-nvidia-dinesh-majrekar-civo-kim-wustkamp-killercoda-peter-salanki-coreweave
youtube_search_url: https://www.youtube.com/results?search_query=Notes+from+the+Field%3A+A+Discussion+with+the+KubeVirt+End+Users+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Notes from the Field: A Discussion with the KubeVirt End Users - Alona Paz, Red Hat; Ryan Hallisey, Nvidia; Dinesh Majrekar, Civo; Kim Wüstkamp, Killercoda; Peter Salanki, CoreWeave

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alona Paz, Red Hat, Ryan Hallisey, Nvidia, Dinesh Majrekar, Civo, Kim Wüstkamp, Killercoda, Peter Salanki, CoreWeave
- Schedule: https://kccnceu2023.sched.com/event/1HyRz/notes-from-the-field-a-discussion-with-the-kubevirt-end-users-alona-paz-red-hat-ryan-hallisey-nvidia-dinesh-majrekar-civo-kim-wustkamp-killercoda-peter-salanki-coreweave
- Busca YouTube: https://www.youtube.com/results?search_query=Notes+from+the+Field%3A+A+Discussion+with+the+KubeVirt+End+Users+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Notes from the Field: A Discussion with the KubeVirt End Users.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyRz/notes-from-the-field-a-discussion-with-the-kubevirt-end-users-alona-paz-red-hat-ryan-hallisey-nvidia-dinesh-majrekar-civo-kim-wustkamp-killercoda-peter-salanki-coreweave
- YouTube search: https://www.youtube.com/results?search_query=Notes+from+the+Field%3A+A+Discussion+with+the+KubeVirt+End+Users+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7LuzKvnMdpk
- YouTube title: Notes from the Field: A Discussion with the...- A Paz, R Hallisey, D Majrekar, K Wüstkamp, P Salanki
- Match score: 0.725
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/notes-from-the-field-a-discussion-with-the-kubevirt-end-users/7LuzKvnMdpk.txt
- Transcript chars: 33763
- Keywords: virtual, actually, machines, running, machine, create, cluster, device, network, workload, provide, similar, access, migrate, networking, infrastructure, gpu, nvidia

### Resumo baseado na transcript

hi everyone welcome to notes from the field the discussion with the cube root end users I'm Alana Paz I'm a principal software engineer at redhead I'm part of the cube root networking team and the maintenance redhead and so before we start I want to ask the audience a small question can any of you that heard about cube root in the past raised their hand okay makes sense you're here and the can the ones that actually used it raise their hand okay nice nice so I'll briefly

### Excerpt da transcript

hi everyone welcome to notes from the field the discussion with the cube root end users I'm Alana Paz I'm a principal software engineer at redhead I'm part of the cube root networking team and the maintenance redhead and so before we start I want to ask the audience a small question can any of you that heard about cube root in the past raised their hand okay makes sense you're here and the can the ones that actually used it raise their hand okay nice nice so I'll briefly present what is cube root and then we'll go to the panelists and so cube root is an add-on to kubernetes it extends kubernetes with resource types for virtual machines it enables running virtual machines alongside pods in a kubernetes cluster actually the pod is having the virtual machine inside it and the virtual machine is connected to the Pod networking so the virtual machine is connected to the Pod networking so the virtual machine has communication to the cluster Network any component in the cluster can communicate with the virtual machine and the virtual machine can communicate with any component in the cluster that is communicating with the cluster Network managing the virtual machines is done using the same standard tools that kubernetes has like Cube CTL so let's go to our panelists say can you please present yourself where are you working for what company what is your role in the company and what your company is doing so I'm Ryan Halsey I'm a software engineer at Nvidia and I'm sure everyone knows what Nvidia is here but if you don't Nvidia makes gpus performance various services around those gpus and so I specifically work on a product called GeForce now and GeForce now is uh cloud gaming service and so if you uh what do you think about it is if you ever wanted to get access to like a 3080 and you wanted to stream a game on it over Wi-Fi in any device anywhere you could do that using GeForce now and so specifically I work on the infrastructure as a part of GeForce now hi good morning my name is Dinesh madraker I am CTO at sivo we're a cloud native service provider who are providing kubernetes clusters in infrastructure that we manage around the world uh focused on delivery developer experience uh being really really simple cost effective and kind of reimagining how cloud computing is being provided today yes hi my name is Kim I'm the founder of killer quota we are a very recent startup we only exist since one and a half years and we provide sandbox environments so you can just i
