---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Charalampos Mainas", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFwj/project-lightning-talk-urunc-the-new-kid-in-the-block-of-sandboxed-container-runtimes-charalampos-mainas-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Urunc%3A+The+New+Kid+In+The+Block+Of+Sandboxed+Container+Runtimes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Urunc: The New Kid In The Block Of Sandboxed Container Runtimes - Charalampos Mainas, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Charalampos Mainas, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFwj/project-lightning-talk-urunc-the-new-kid-in-the-block-of-sandboxed-container-runtimes-charalampos-mainas-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Urunc%3A+The+New+Kid+In+The+Block+Of+Sandboxed+Container+Runtimes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Urunc: The New Kid In The Block Of Sandboxed Container Runtimes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFwj/project-lightning-talk-urunc-the-new-kid-in-the-block-of-sandboxed-container-runtimes-charalampos-mainas-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Urunc%3A+The+New+Kid+In+The+Block+Of+Sandboxed+Container+Runtimes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XCzaeoqHya4
- YouTube title: Project Lightning Talk: Urunc: The New Kid In The Block Of Sandboxed Container... Charalampos Mainas
- Match score: 0.969
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-urunc-the-new-kid-in-the-block-of-sandboxed-con/XCzaeoqHya4.txt
- Transcript chars: 5075
- Keywords: containers, sandbox, container, application, monitor, around, isolation, sandboxed, specific, scenarios, workloads, deploy, inside, sidecar, therefore, environments, wednesday, runtimes

### Resumo baseado na transcript

Uh I am Haralamus but you can just call me >> talk into the mic please. I am Haralamus but you can just call me uh Bobby uh for simplicity and I'm one of the creators and maintainers of Uran C uh the project that I'm going to talk to you about this couple five minutes. So let's see uh a bit in a in a Kubernetes uh how that looks uh so you can better understand exactly the difference between other sandbox container runtimes.

### Excerpt da transcript

Hello everyone. Uh I am Haralamus but you can just call me >> talk into the mic please. >> Okay. I am Haralamus but you can just call me uh Bobby uh for simplicity and I'm one of the creators and maintainers of Uran C uh the project that I'm going to talk to you about this couple five minutes. So as we know the struggle is real like we have uh on one side we like containers because they uh we like containers because they are fast they are easy to use. we have a bunch of ecosystem around it but on the same time we don't really trust them for uh some specific scenarios where we care about isolation like multi-tenency or for example AI sandboxing and in this kind scenarios we want some stronger isolation like VM and when we do that we lose performance and we lose other kind of stuff so with urine C we aim to solve this kind of stuff uh is a CNCF sandbox project that is a CRI compatible runtime which means it has seamless integration ation with the rest of the container uh ecosystem. And it's uh focusing on what we call uh single application workloads in the form of uni kernels or uh single application kernels which means that we package our application alongside with a kernel where we deploy uh this uh uh workload and the context here is that we create a container and inside this container we create a sandbox.

This sandbox can come in the form of a softwarebased sandbox. Think about it like G visor or in the form of an actual virtual machine. So let's see uh a bit in a in a Kubernetes uh how that looks uh so you can better understand exactly the difference between other sandbox container runtimes. So in a in a pod deployment we have this uh pods we have the sidecar containers and we have the user containers. The sidecar containers might be uh containers that we deploy as the platform while the user containers are containers that we don't trust. We don't know what they do and we want to isolate them from the rest of the uh host and of the other containers. And that's what uran does. UNC treats the sidecar containers as normal containers while the user containers are treated as untrusted and therefore they have to be isolated in a secure sandbox. This sandbox can be in the form of a softwarebased sandbox or in the case of virtual machine and URC sets up this containerized environment for that particular uh monitor.

We call the sandbox monitor as monitor and inside the sandbox we have the application running as for example in a VM. Think about it as the init b
