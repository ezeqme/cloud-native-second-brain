---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Tutorials"
themes: ["AI ML"]
speakers: ["Lin Sun", "Krisztian Fekete", "Denis Jannot", "solo.io"]
sched_url: https://kccnceu2024.sched.com/event/1YeQr/tutorial-simpler-than-making-a-fraisier-cake-building-running-and-observing-your-first-ebpf-program-lin-sun-krisztian-fekete-denis-jannot-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Simpler+Than+Making+a+Fraisier+Cake%3A+Building%2C+Running%2C+and+Observing+Your+First+eBPF+Program+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tutorial: Simpler Than Making a Fraisier Cake: Building, Running, and Observing Your First eBPF Program - Lin Sun, Krisztian Fekete & Denis Jannot, solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Tutorials]]
- Temas: [[AI ML]]
- País/cidade: France / Paris
- Speakers: Lin Sun, Krisztian Fekete, Denis Jannot, solo.io
- Schedule: https://kccnceu2024.sched.com/event/1YeQr/tutorial-simpler-than-making-a-fraisier-cake-building-running-and-observing-your-first-ebpf-program-lin-sun-krisztian-fekete-denis-jannot-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Simpler+Than+Making+a+Fraisier+Cake%3A+Building%2C+Running%2C+and+Observing+Your+First+eBPF+Program+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tutorial: Simpler Than Making a Fraisier Cake: Building, Running, and Observing Your First eBPF Program.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQr/tutorial-simpler-than-making-a-fraisier-cake-building-running-and-observing-your-first-ebpf-program-lin-sun-krisztian-fekete-denis-jannot-soloio
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Simpler+Than+Making+a+Fraisier+Cake%3A+Building%2C+Running%2C+and+Observing+Your+First+eBPF+Program+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lpopvZ67l6I
- YouTube title: Tutorial: Simpler Than Making a Fraisier Cake: Building, Running, and Observing Your First eBPF...
- Match score: 1.038
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tutorial-simpler-than-making-a-fraisier-cake-building-running-and-obse/lpopvZ67l6I.txt
- Transcript chars: 69265
- Keywords: program, ebpf, kernel, basically, bumblebee, actual, memory, process, itself, running, information, mentioned, deploy, buffer, little, question, cluster, workshop

### Resumo baseado na transcript

okay so let's start I think we'll have a few slides at the beginning so even if people are a little bit late they will uh be on time for the for the workshop so uh hi everyone my name is uh Deno I am uh director of the solution engineering team in um EMA at solo.io um I'm going to present the workshop with Christian you want to introduce yourself yes hello everyone my name is chrisan feta I'm working in Denny team in the European field engineering team kernel propes in the kernel that will be most certainly uh passed in uh during execution when an outof memory event happens without this there are some metrics there are some other approaches to uh get out of memory exceptions but you might not be counter here because we want to expose this as promi speci because we are building an killer uh and umill exporter um okay after this in the actual code section uh we are attaching this custom logic to the very same Cel problem that we

### Excerpt da transcript

okay so let's start I think we'll have a few slides at the beginning so even if people are a little bit late they will uh be on time for the for the workshop so uh hi everyone my name is uh Deno I am uh director of the solution engineering team in um EMA at solo.io um I'm going to present the workshop with Christian you want to introduce yourself yes hello everyone my name is chrisan feta I'm working in Denny team in the European field engineering team and yeah we were doing this uh workshop together and L is apologizing she's not able to join but she worked uh with us uh to prepare the workshop so want to say thank you to to her um what we are going to do uh as we as I said uh for the people who are already there we are going to go through a few slid to introduce uh the main ebpf Concepts and um then we are going to use instruct uh platform for doing the workshop so you will all have access to this uh Workshop we are going to share again the link in uh in a few minutes perhaps we can do it perhaps you can do it now if while I speak yeah um and please don't click on start because if you click on start it's going to provision everything and then if you don't use it for some time it times out and you know when uh when we are going to be ready to start then it will be uh you will have to do it again so uh the start should be quite quick anyway uh as I was mentioning for people who are not there at that time uh we give you many options you can either just watch us doing it or you can do it at the same time we do it or you can use the same this link until Sunday evening if you want to do it later right so it's uh it's quite flexible um so I think we can just uh get started and uh also we want to try to make it interactive we have 90 minutes which is quite good amount of time to be able to take our time and if you have any question uh you you can just um you know do go through these microphones that there's one here and I think they may one one there as well so if you have any question really feel free uh to uh raise your hand and go to these uh microphones we'll try to make some breaks at some point just to give you time to ask questions like perhaps at the end of the slide for example uh but yeah we we we will try to make it interactive even if it's complicated with so many people in the room uh but yeah we we really want to try to answer any question you you may have so Christian the floor is yours all right so as D mentioned we have a few introductory slides
