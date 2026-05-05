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
speakers: ["Sascha Grunert", "Swati Sehgal", "Red Hat", "Alexander Kanevskiy", "Intel", "Evan Lezar", "NVIDIA", "David Porter", "Google"]
sched_url: https://kccnceu2023.sched.com/event/1HyVB/node-resource-management-the-big-picture-sascha-grunert-swati-sehgal-red-hat-alexander-kanevskiy-intel-evan-lezar-nvidia-david-porter-google
youtube_search_url: https://www.youtube.com/results?search_query=Node+Resource+Management%3A+The+Big+Picture+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Node Resource Management: The Big Picture - Sascha Grunert & Swati Sehgal, Red Hat; Alexander Kanevskiy, Intel; Evan Lezar, NVIDIA; David Porter, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Runtime Performance + Constrained Environments]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Sascha Grunert, Swati Sehgal, Red Hat, Alexander Kanevskiy, Intel, Evan Lezar, NVIDIA, David Porter, Google
- Schedule: https://kccnceu2023.sched.com/event/1HyVB/node-resource-management-the-big-picture-sascha-grunert-swati-sehgal-red-hat-alexander-kanevskiy-intel-evan-lezar-nvidia-david-porter-google
- Busca YouTube: https://www.youtube.com/results?search_query=Node+Resource+Management%3A+The+Big+Picture+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Node Resource Management: The Big Picture.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyVB/node-resource-management-the-big-picture-sascha-grunert-swati-sehgal-red-hat-alexander-kanevskiy-intel-evan-lezar-nvidia-david-porter-google
- YouTube search: https://www.youtube.com/results?search_query=Node+Resource+Management%3A+The+Big+Picture+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LjhgklNNAtA
- YouTube title: Node Resource Management: The Big Picture
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/node-resource-management-the-big-picture/LjhgklNNAtA.txt
- Transcript chars: 29944
- Keywords: resource, resources, container, memory, manager, topology, features, actually, runtime, gpu, management, components, around, feature, devices, mentioned, dynamic, access

### Resumo baseado na transcript

good morning Amsterdam good morning cubecon I hope you are energetic today after working out sessions and uh today we are one of our first sessions and we are starting as a panel discussion and as you might assume the panel is uh something what should be interactive and we as a panelists on this session we are expecting what audiences asking questions so as soon as you have questions you want to ask something please raise your hand and our helper in the room will bring your microphone feel not every single container out there is probably using CPU and memory which are the core kind of kubernetes resources right and so underpinning pods and container resources uh with CPU and memory are c groups so c groups are the Linux kernel feature that so uh secret V1 was kind of the first iteration of the C group API and it's what everybody was using and so very recently in the ecosystem secret V2 has been starting out and we're really happy to announce it was G8 and kubernetes so secret V2 is a new kind of platform and so it has many new Resource Management capabilities that we're kind of hoping to take advantage in kubernetes to provide more enhanced Resource Management capabilities so some of the example I want to highlight kind of the few projects that we're working on in the signode community that are kind of built on top of the secret V2 platform one of them is memory qos this is...

### Excerpt da transcript

good morning Amsterdam good morning cubecon I hope you are energetic today after working out sessions and uh today we are one of our first sessions and we are starting as a panel discussion and as you might assume the panel is uh something what should be interactive and we as a panelists on this session we are expecting what audiences asking questions so as soon as you have questions you want to ask something please raise your hand and our helper in the room will bring your microphone feel free to ask anything in my area and today we got panelists many of us from different companies working on different areas um a lot of new topics a lot of new changes in the past year in our area so let me first introduce myself and when all my colleagues here on stage I am Alexander kanevsky I work for Intel I am part of a team who is working on Resource Management topics mostly so runtime Google it and related projects like node feature discovering hi everyone I am Swati sehgal I am working as a principal software engineer in the ecosystem Engineering Group at Red Hat I've been involved in the resource management space as well for a while just like Sasha and my focus has been Numa awareness and Resource Management capability especially the cubital resource managers and looking forward to having questions from you guys hi good morning I'm Ivan Lazar I'm with Nvidia a part of the cloud native group group there well I just try to get gpus and other funky devices to work in containerized environments so that's why I'm here hello everyone thanks for coming my name is David Porter I'm from the Google kubernetes engine team I work on node I also work in Upstream cignode Community I'm the maintainer of a seat advisor which does research management monitoring and I focus a lot in the research management space so really excited for this panel hey folks I'm Zasha I'm considering myself as an upstream contributor to kubernetes so I'm working in sick node and also sick release I'm also one of the maintenance of cryo the container runtime you may know it and I really enjoy I really hope that you enjoyed this coupon and it's great to see all of you all right to start with discussion uh a big picture uh the features What in in the area are present in kubernetes for quite some years so we all know where distribution of a functionality between the control plane like a scheduler pickups we know and keep struggling for resources on the nodes and when we have kublet uh with set of managers
