---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML"]
speakers: ["C. A. Fillekes", "WG Chair"]
sched_url: https://kccnceu2025.sched.com/event/1tcvQ/project-lightning-talk-multi-arch-kubevirt-and-cdi-c-a-fillekes-wg-chair
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Multi-Arch+KubeVirt+and+CDI+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Multi-Arch KubeVirt and CDI - C. A. Fillekes, WG Chair

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]]
- País/cidade: United Kingdom / London
- Speakers: C. A. Fillekes, WG Chair
- Schedule: https://kccnceu2025.sched.com/event/1tcvQ/project-lightning-talk-multi-arch-kubevirt-and-cdi-c-a-fillekes-wg-chair
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Multi-Arch+KubeVirt+and+CDI+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Multi-Arch KubeVirt and CDI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvQ/project-lightning-talk-multi-arch-kubevirt-and-cdi-c-a-fillekes-wg-chair
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Multi-Arch+KubeVirt+and+CDI+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Je6GIoagHvU
- YouTube title: Project Lightning Talk: Multi-Arch KubeVirt and CDI - C. A. Fillekes, WG Chair
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-multi-arch-kubevirt-and-cdi/Je6GIoagHvU.txt
- Transcript chars: 4134
- Keywords: machines, virtual, containerized, importer, architectures, obviously, vmware, mainframe, worker, multi-arch, multi-archch, working, cubert, container, feature, import, upload, storage

### Resumo baseado na transcript

I'm here to talk about a multi-archch cube and containerized data importer on uh multiple architectures obviously. I'm at IBM systems working as a Red Hat partner engineer for about five years now. what is S390X architecture also known as the IBM mainframe and it's like do we use IBM mainframes anymore and the answer is about 97% of your credit card transactions are processed by an IBM mainframe so that yes they are in wide use uh they also run at low power they also uh are reduced instruction set their big Indian which uh is reporting issues they run then there's a many many uh features that in addition to porting say uh Kubernetes andor uh Cubver andor CDI to the S390X uh architecture, you've also got all these other wonderful features that you want to enable um in the course of that so that if you get a specialized VM or develop a specialized VM, it runs easily on there. Okay, there's multi-arch which means that you can run this on different machines with different architectures, right?

### Excerpt da transcript

I'm here to talk about a multi-archch cube and containerized data importer on uh multiple architectures obviously. Uh my name is Cheryl Filicus. I'm at IBM systems working as a Red Hat partner engineer for about five years now. Been working on this project for about two years. And uh today's discussion regards the upstream open-source aspect of the project only so that my uh boss doesn't have an aneurysm. Okay. What is Cubert and containerized data importer? Cubert is a is a uh is a way to run KVM virtual machines in a container. Uh this is often used in uh uh Kubernetes clusters. You can stop and start virtual machines with a YAML file, reconfigure, relaunch existing VMs. It's got a nice templating feature. Containerized data importer uses uh persistent volume claims on disks for cubevert VMs by way of data volumes and it can also uh import clone and upload your uh attached storage. Note that CDI import clone and upload are supported for VMs which are among other storage options stored externally in VMware installations via the virtual disc development toolkit on x86 and on x86 alone.

This this uh will come in to be important in our next slide. Uh what do I mean by different architectures? I mean uh your x86 machines that are in widespread use in data centers across the world. Uh they run Linux, RH Core OS, you've got a lot of VM templates, a lot of VMs for them. Uh container registries galore. Uh and uh Kubernetes obviously runs really well on these. ARM 64. You've got all of those things except also they run at about half the power per CPU cycle. They're reduced instruction set run on uh uh L excuse me little Indian encoding just like x86 and uh these these are your usual uh Mac uh Raspberry Pi cell phones and edge devices. So this is out at the edge very often but also in big server rooms as well these days. Okay. what is S390X architecture also known as the IBM mainframe and it's like do we use IBM mainframes anymore and the answer is about 97% of your credit card transactions are processed by an IBM mainframe so that yes they are in wide use uh they also run at low power they also uh are reduced instruction set their big Indian which uh is reporting issues they run then there's a many many uh features that in addition to porting say uh Kubernetes andor uh Cubver andor CDI to the S390X uh architecture, you've also got all these other wonderful features that you want to enable um in the course of that so that if you get a specialized VM or develop a s
