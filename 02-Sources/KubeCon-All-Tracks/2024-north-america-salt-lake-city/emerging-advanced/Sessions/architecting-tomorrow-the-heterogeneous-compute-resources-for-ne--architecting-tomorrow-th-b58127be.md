---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Emerging + Advanced"
themes: ["Emerging + Advanced"]
speakers: ["Alexander Kanevskiy", "Intel Finland"]
sched_url: https://kccncna2024.sched.com/event/1i7ke/architecting-tomorrow-the-heterogeneous-compute-resources-for-new-types-of-workloads-alexander-kanevskiy-intel-finland
youtube_search_url: https://www.youtube.com/results?search_query=Architecting+Tomorrow%3A+The+Heterogeneous+Compute+Resources+for+New+Types+of+Workloads+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Architecting Tomorrow: The Heterogeneous Compute Resources for New Types of Workloads - Alexander Kanevskiy, Intel Finland

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Emerging + Advanced]]
- País/cidade: United States / Salt Lake City
- Speakers: Alexander Kanevskiy, Intel Finland
- Schedule: https://kccncna2024.sched.com/event/1i7ke/architecting-tomorrow-the-heterogeneous-compute-resources-for-new-types-of-workloads-alexander-kanevskiy-intel-finland
- Busca YouTube: https://www.youtube.com/results?search_query=Architecting+Tomorrow%3A+The+Heterogeneous+Compute+Resources+for+New+Types+of+Workloads+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Architecting Tomorrow: The Heterogeneous Compute Resources for New Types of Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ke/architecting-tomorrow-the-heterogeneous-compute-resources-for-new-types-of-workloads-alexander-kanevskiy-intel-finland
- YouTube search: https://www.youtube.com/results?search_query=Architecting+Tomorrow%3A+The+Heterogeneous+Compute+Resources+for+New+Types+of+Workloads+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jyovyLafMOs
- YouTube title: Architecting Tomorrow: The Heterogeneous Compute Resources for New Types of Workloads - A. Kanevskiy
- Match score: 1.013
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/architecting-tomorrow-the-heterogeneous-compute-resources-for-new-type/jyovyLafMOs.txt
- Transcript chars: 25295
- Keywords: memory, hardware, device, workload, actually, workloads, processors, devices, socket, happening, standard, controller, protocol, understand, running, trying, application, generation

### Resumo baseado na transcript

so welcome everyone uh let's start breakout sessions of this cubec Con of America 24 uh I'm Alexander kvki uh I work for Intel and I will today talk about a lot about the internal ofare Hardware how it affects the workload and vice versa so even though I'm not going to show any particular performance number but what you need to understand is what performance is think uh relative and like there is no single solution which serves everyone so be careful with all this like statements or understanding

### Excerpt da transcript

so welcome everyone uh let's start breakout sessions of this cubec Con of America 24 uh I'm Alexander kvki uh I work for Intel and I will today talk about a lot about the internal ofare Hardware how it affects the workload and vice versa so even though I'm not going to show any particular performance number but what you need to understand is what performance is think uh relative and like there is no single solution which serves everyone so be careful with all this like statements or understanding what what I am saying um I will be talking about Intel processors but at the same time I also will cover few things what is coming from our vendor so like what is in modern arm world what the AMD is doing and so on so all trade marks all copyrights are related to them so first of all uh why I am speaking about that uh I'm Hardware engineer by education but all of my career I I'm working on the system software level and currently I'm in Intel uh I'm principal engineer um last six or so years I'm working primarily on the things related to Performance optimizations platform enablement um power optimizations and so on so all of these things related to like lowlevel things like runtime innative stocks um all device enablement device plugins Dr and so on I'm more or less involved in all of those uh in the past years so I hope my experience is good enough to to explain what is happening on my Hardware level um why I'm talking about that what reason is primarily because the ecosystem of workloads what we are running on top of our cloud is changing rapidly uh and most of the time unfortunately the cncf ecosystem is not prepared to drastic change of War Cloud patterns so we knew what AI is coming it was small models it was usage of accelerators usage on CPU but when generative AI came and we realize that what whatever we have in device plugins was not enough but this is how a DA was born um same happens actually in the CPU it's not that easily visible so every year we run new technologies where are new new ances what is coming and and again unfortunately cncf system uh ecosystem is not really prepared to be evolving as fast as with technology so it's surprisingly it now takes longer to create the software option for something when actually create the hardware for something so the reason why I'm talking is mostly let's think about like how CPUs and how peripheral devices are changes and let's think about how uh user experience will be in the future let's be prepared this tim
