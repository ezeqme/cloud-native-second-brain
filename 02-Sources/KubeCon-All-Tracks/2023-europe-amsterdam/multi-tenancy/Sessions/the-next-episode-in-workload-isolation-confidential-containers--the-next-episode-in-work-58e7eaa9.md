---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Multi-tenancy"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Jeremi Piotrowski", "Microsoft"]
sched_url: https://kccnceu2023.sched.com/event/1HyaJ/the-next-episode-in-workload-isolation-confidential-containers-jeremi-piotrowski-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=The+Next+Episode+in+Workload+Isolation%3A+Confidential+Containers+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The Next Episode in Workload Isolation: Confidential Containers - Jeremi Piotrowski, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Multi-tenancy]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jeremi Piotrowski, Microsoft
- Schedule: https://kccnceu2023.sched.com/event/1HyaJ/the-next-episode-in-workload-isolation-confidential-containers-jeremi-piotrowski-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=The+Next+Episode+in+Workload+Isolation%3A+Confidential+Containers+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The Next Episode in Workload Isolation: Confidential Containers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyaJ/the-next-episode-in-workload-isolation-confidential-containers-jeremi-piotrowski-microsoft
- YouTube search: https://www.youtube.com/results?search_query=The+Next+Episode+in+Workload+Isolation%3A+Confidential+Containers+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rb08ubfJQSM
- YouTube title: The Next Episode in Workload Isolation: Confidential Containers - Jeremi Piotrowski, Microsoft
- Match score: 0.896
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-next-episode-in-workload-isolation-confidential-containers/rb08ubfJQSM.txt
- Transcript chars: 25578
- Keywords: confidential, containers, attestation, hardware, measurement, trusted, hypervisor, launch, computing, execution, environment, called, nested, station, report, working, evidence, inside

### Resumo baseado na transcript

thank you everyone for coming to my talk my name is Jeremy piotrovski I work for Microsoft and the title of this talk is the next episode in workload isolation confidential containers at the start of this talk I'd like to talk just briefly about myself just so that you know where I'm coming from and what my background is so I started working in embedded Linux systems and Hardware security modules I'm the maintainer of the or one of the maintainers of the flat car container Linux project I've it gives a challenge to the T expects this to be included in the in the attestation report right so that it knows that the t is actually in control of the attestation procedure the other use case is to include some kind of key

### Excerpt da transcript

thank you everyone for coming to my talk my name is Jeremy piotrovski I work for Microsoft and the title of this talk is the next episode in workload isolation confidential containers at the start of this talk I'd like to talk just briefly about myself just so that you know where I'm coming from and what my background is so I started working in embedded Linux systems and Hardware security modules I'm the maintainer of the or one of the maintainers of the flat car container Linux project I've been working for Microsoft in Azure for the last two years and for the last year I've been working on confidential containers and within the confidential containers project if you want to reach me after the talk with questions follow up anything that's my email my scad profile contains other socials but that's the that's the reliable one or slack I'm on the cncf slack on the kubecon slack and the focus of this talk will be a project called confidential containers right we often refer to it as Coco just because it's nice it's short and cute and Coco is a cncf Sandbox project it is built on top of Kata containers a project with which many of you may be familiar um yeah Kata containers is used to isolate work clothes using VMS and confidential containers isolates workloads using confidential VMS it's a fairly young project so I think it's been around for some two years in the cncf since a year we're currently at the 0.50 release which happened last week was very exciting and the the goal of the project is to enable Cloud native confidential Computing by leveraging trusted execution environments to protect containers and data right and so this talk will really talk about the different aspects of that mission if you want to find out more about the project about the community that's the GitHub link to the community repo it links to the various you know documentation repos and and code and the thing about confidential containers is that every single thing about it is interesting right there are challenges everywhere everything could be a 30 minute talk right and so I can't cover everything maybe for the better but there was a talk earlier today like right before lunch uh by Fabiana fidencio and Jens freiman also two confidential containers community members um if you weren't there review it offline later it was great and give you an intro into like the architecture of the confidential containers project if you're more interested in Kata containers itself there's a talk later
