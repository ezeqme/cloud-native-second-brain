---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Runtimes"
themes: ["Runtime Containers"]
speakers: ["Antti Kervinen", "Intel", "Peter Hunt", "Red Hat"]
sched_url: https://kccncna2021.sched.com/event/m4t2/do-not-disturb-mode-fine-tuning-resources-for-latency-sensitive-workloads-antti-kervinen-intel-peter-hunt-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Do+Not+Disturb+Mode%3A+Fine-Tuning+Resources+for+Latency+Sensitive+Workloads+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Do Not Disturb Mode: Fine-Tuning Resources for Latency Sensitive Workloads - Antti Kervinen, Intel & Peter Hunt, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Runtimes]]
- Temas: [[Runtime Containers]]
- País/cidade: United States / Los Angeles
- Speakers: Antti Kervinen, Intel, Peter Hunt, Red Hat
- Schedule: https://kccncna2021.sched.com/event/m4t2/do-not-disturb-mode-fine-tuning-resources-for-latency-sensitive-workloads-antti-kervinen-intel-peter-hunt-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Do+Not+Disturb+Mode%3A+Fine-Tuning+Resources+for+Latency+Sensitive+Workloads+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Do Not Disturb Mode: Fine-Tuning Resources for Latency Sensitive Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/m4t2/do-not-disturb-mode-fine-tuning-resources-for-latency-sensitive-workloads-antti-kervinen-intel-peter-hunt-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Do+Not+Disturb+Mode%3A+Fine-Tuning+Resources+for+Latency+Sensitive+Workloads+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2ILD_Kwju0w
- YouTube title: Do Not Disturb Mode: Fine-Tuning Resources for Latency Sensitive Workloads - A Kervinen & P Hunt
- Match score: 0.97
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/do-not-disturb-mode-fine-tuning-resources-for-latency-sensitive-worklo/2ILD_Kwju0w.txt
- Transcript chars: 14782
- Keywords: memory, workloads, priority, configure, resources, process, actually, container, throttle, classes, access, bandwidth, workload, devices, numbers, little, running, scanner

### Resumo baseado na transcript

hello and welcome to do not disturb mode that is fine tuning resources for latency sensitive sensitive workloads my name is antigeraviden i work for intel and i've been working on resource management especially on the cri and oci runtimes hello my name is peter hunt i'm a software engineer at red hat working primarily on cryo but also on things in sigmod and other computer computer-related technologies and i we also wanted to send a special shout out this uh presentation and work was partially brought to you by

### Excerpt da transcript

hello and welcome to do not disturb mode that is fine tuning resources for latency sensitive sensitive workloads my name is antigeraviden i work for intel and i've been working on resource management especially on the cri and oci runtimes hello my name is peter hunt i'm a software engineer at red hat working primarily on cryo but also on things in sigmod and other computer computer-related technologies and i we also wanted to send a special shout out this uh presentation and work was partially brought to you by marcus letzman who also works at intel i get the integration and design of the rdp work that we're going to describe a little bit so to start off we're going to describe talk a little bit about qos or quality of service and kubernetes since the beginning kubernetes has provided knobs to configure how different workloads are prioritized and how they're configured to run on the node so the qos classes were used to specify memory limits and cpu limits as well as boom killing behavior for different pods and this behavior was able to be further customized by cpu management policies to be able to configure which cpus workloads ended up on which allows for users to configure cpu affinity so that there is a noisy neighbor problem among different workloads but this uh leaves a lot of other resources that exist on the node but aren't quite as possible to configure and this uh causes workloads to be disturbed when it would be a little bit better if they were less disturbed and were given more access to those resources and were less latent so cryo has recently and there's a pr and continuity as well but in cryo1.22 we have uh the capability of configuring uh two new resources um this the first one is intel's resource director technology or rdt it is a way to configure cache and memory bandwidth so you can think of it as finer grading control over the way that memory and the memory bandwidth in the cpu cache are configured and next we have the capability of configuring block i o classes in a similar way as the qos class this gets class based uh you know on a c group granularity block io uh controller so you can configure how given a c group you can figure how that c group is able to the scheduler is going to prioritize it you can give it extra weight or you can throttle that workload so that it can only access a certain amount of the block i o so let's describe you know the situation before any of this qos stuff so we have our three workloads running on the same
