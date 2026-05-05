---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Platform Engineering", "Sustainability"]
speakers: ["Leonard Pahlke", "University of Applied Sciences Hamburg"]
sched_url: https://kccnceu2024.sched.com/event/1YeOO/unlock-energy-consumption-in-the-cloud-with-ebpf-leonard-pahlke-university-of-applied-sciences-hamburg
youtube_search_url: https://www.youtube.com/results?search_query=Unlock+Energy+Consumption+in+the+Cloud+with+eBPF+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Unlock Energy Consumption in the Cloud with eBPF - Leonard Pahlke, University of Applied Sciences Hamburg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Sustainability]]
- País/cidade: France / Paris
- Speakers: Leonard Pahlke, University of Applied Sciences Hamburg
- Schedule: https://kccnceu2024.sched.com/event/1YeOO/unlock-energy-consumption-in-the-cloud-with-ebpf-leonard-pahlke-university-of-applied-sciences-hamburg
- Busca YouTube: https://www.youtube.com/results?search_query=Unlock+Energy+Consumption+in+the+Cloud+with+eBPF+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Unlock Energy Consumption in the Cloud with eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOO/unlock-energy-consumption-in-the-cloud-with-ebpf-leonard-pahlke-university-of-applied-sciences-hamburg
- YouTube search: https://www.youtube.com/results?search_query=Unlock+Energy+Consumption+in+the+Cloud+with+eBPF+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lW9pZoKRJVs
- YouTube title: Unlock Energy Consumption in the Cloud with eBPF - Leonard Pahlke
- Match score: 0.945
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/unlock-energy-consumption-in-the-cloud-with-ebpf/lW9pZoKRJVs.txt
- Transcript chars: 26366
- Keywords: energy, consumption, software, resources, hardware, information, metrics, resource, operating, basically, little, consume, deploy, ebpf, capabilities, getting, kepler, layers

### Resumo baseado na transcript

all right um thank you everybody for joining thank you for taking the time um I hope you all have a great Cube con so far um today I will talk about uh energy and Cloud an emerging field very new very exciting uh I hope uh you all get something out of out of it uh maybe you can um move some of the learnings to your companies to your projects um we will see but um you you don't need to be like an expert you don't need

### Excerpt da transcript

all right um thank you everybody for joining thank you for taking the time um I hope you all have a great Cube con so far um today I will talk about uh energy and Cloud an emerging field very new very exciting uh I hope uh you all get something out of out of it uh maybe you can um move some of the learnings to your companies to your projects um we will see but um you you don't need to be like an expert you don't need to know much about uh resource consumption and Cloud um this talk is very much giving like a proper or good introduction um what it is all about so we will explore all the layers sort of I think it makes a lot of sense looking at the layers and at the end we will reach like the cloud layer and then we will kind of figure out what our our requirements in the cloud when it comes to resources and um energy so my name is Leo I'm one of the chairs for the cncf technical Advisory Group for environmental sustainability you may have seen Cen us we have booth there was also maintainer talk earlier today so um if you like to chat with us um Tomorrow there's also the booth still open come step by um would be great to talk to you so I think first things first um like the obvious question why should I care about resources why should I care uh about energy um and I think this is like a very common pattern in software that we we are the software people we don't really care about the hardware side of things right we don't this is like data centers resources all of this it's like we we choose to build software we don't want to be uh involved too much with Hardware so I think it's like also like my mindset when I started building software that um I I choose this path um I like software engineering and I'm not a hardware guy I'm a software guy um but I think um so over the time um that um this attitude sort of that we are so disconnected from the hardware from the resources at some point will will bite us a little bit um so I think it's going fine uh right now but I think we should be a little bit more aware of the resources that we um consume especially if we build Innovative Technologies like blockchain stuff AI stuff all of this which is very good in a lot of aspects but in terms of resource consumption it's terrible so it would be great to invent those tools but a little bit more resource efficient so um I think in general um to move this space forward we will not get rid of software we will build more software but the software that we build sort of also inc
