---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Kubernetes Core"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW9K/eraser-cleaning-up-vulnerable-images-from-kubernetes-nodes-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Eraser%3A+Cleaning+Up+Vulnerable+Images+from+Kubernetes+Nodes+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Eraser: Cleaning Up Vulnerable Images from Kubernetes Nodes | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW9K/eraser-cleaning-up-vulnerable-images-from-kubernetes-nodes-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Eraser%3A+Cleaning+Up+Vulnerable+Images+from+Kubernetes+Nodes+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Eraser: Cleaning Up Vulnerable Images from Kubernetes Nodes | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW9K/eraser-cleaning-up-vulnerable-images-from-kubernetes-nodes-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Eraser%3A+Cleaning+Up+Vulnerable+Images+from+Kubernetes+Nodes+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=l_RzR8X62S8
- YouTube title: Eraser: Cleaning Up Vulnerable Images from Kubernetes Nodes | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/eraser-cleaning-up-vulnerable-images-from-kubernetes-nodes-project-lig/l_RzR8X62S8.txt
- Transcript chars: 3323
- Keywords: eraser, images, container, removal, scanner, custom, remove, cluster, questions, runtime, support, memory, vulnerable, address, pluggable, schedules, answer, running

### Resumo baseado na transcript

okay hi everyone my name is Ashna and I'm a maintainer for eraser and a software engineer at Microsoft and today I'm going to be talking about eraser and some of the things that we've been working on so eraser is a cncf Sandbox project and it's a tool to help you remove a list of non-running images from the nodes in your cluster so I'm sure we've all had cves arising from old and stale images and eraser helps you address these images by a manual Trigger or automated

### Excerpt da transcript

okay hi everyone my name is Ashna and I'm a maintainer for eraser and a software engineer at Microsoft and today I'm going to be talking about eraser and some of the things that we've been working on so eraser is a cncf Sandbox project and it's a tool to help you remove a list of non-running images from the nodes in your cluster so I'm sure we've all had cves arising from old and stale images and eraser helps you address these images by a manual Trigger or automated removal and what distinguishes eraser is the control it provides you over the removal so you can customize it with things like a repeat period excluding certain images and nodes from removal and also having a pluggable scanner so eraser schedules eraser pods on each node and and each of the pods aim to answer three questions the first is what images are present on this node second is of those images which are not tied to a container that is currently running and of those images which contain a known cve meaning we should remove it from our cluster so this is a diagram of how eraser works and the top half is just the scheduling of the eraser pods so eraser creates a custom crd or image job that runs to completion and schedules the Eraser pods on each node and we'll take a look closer into what's happening on each in each of those pods so our pod in is represented in the middle here and each container is referencing those questions that we saw before so the collector container is getting that list of images using the container runtime interface and it's passing on that to the scanner container which is scanning those images for cves and it's using trivy to do that by default but that's pluggable with different scanners and then that the results of that are passed to the remover container which performs the removal again using the container runtime interface so some of the recent features that we've worked on to make erer more user friendly is um adding custom runtime socket configurations adding support for trivy status filtering so you don't have to Target every image that trivy finds a cve in you can make it more targeted to what you want to remove and by refining the arbac we've also decreased the um memory pod the Pod memory by almost 90% um and that helped us address some out of memory issues that the Eraser pod was seeing uh We've also added support for custom pod labels and custom fields for the scanner volume Mount so this lets eraser run in air GED Cloud environments some things that we
