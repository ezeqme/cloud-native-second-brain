---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Research + Academia + HPC + Advanced Concepts"
themes: ["Research + Academia + HPC + Advanced Concepts"]
speakers: ["Atanas Atanasov", "Intel", "Rimma Iontel", "Red Hat"]
sched_url: https://kccnceu2023.sched.com/event/1Hycj/evolution-of-on-node-adaptive-power-tuning-atanas-atanasov-intel-rimma-iontel-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Evolution+of+on-Node+Adaptive+Power+Tuning+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Evolution of on-Node Adaptive Power Tuning - Atanas Atanasov, Intel & Rimma Iontel, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Research + Academia + HPC + Advanced Concepts]]
- Temas: [[Research + Academia + HPC + Advanced Concepts]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Atanas Atanasov, Intel, Rimma Iontel, Red Hat
- Schedule: https://kccnceu2023.sched.com/event/1Hycj/evolution-of-on-node-adaptive-power-tuning-atanas-atanasov-intel-rimma-iontel-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Evolution+of+on-Node+Adaptive+Power+Tuning+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Evolution of on-Node Adaptive Power Tuning.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hycj/evolution-of-on-node-adaptive-power-tuning-atanas-atanasov-intel-rimma-iontel-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Evolution+of+on-Node+Adaptive+Power+Tuning+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_SqebJmYteQ
- YouTube title: Evolution of on-Node Adaptive Power Tuning - Atanas Atanasov, Intel & Rimma Iontel, Red Hat
- Match score: 0.741
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/evolution-of-on-node-adaptive-power-tuning/_SqebJmYteQ.txt
- Transcript chars: 23738
- Keywords: basically, profile, workloads, performance, frequency, manager, workload, profiles, states, configuration, certain, tuning, capabilities, control, running, applications, operator, optimization

### Resumo baseado na transcript

I think we are going to start thank you everybody for making the session I really appreciate you sticking around this long and choosing this session another one next door my name is Rima yontel I'm a Chief Architect responsible for Telco vertical at redhead and yeah thank you very much my name is atanasatanasov I'm senior Cloud native software engineer at Tinto thank you all right and today we are going to talk about power optimization you probably have noticed that sustainability is becoming a Hot Topic and power short demo from my colleague Lucas who is unfortunately not here he recorded something for us to see that in action hi my name is Lucas Daniel joke I'm A Cloud native software engineer at Intel and I'd like to demo the kubernetes paramounter on an openshift platform we will start by verifying that the power manager and the required June the profile are applied we also have a shared profit and performance profile already created note that the performance profile is currently using the performance governor and the third

### Excerpt da transcript

I think we are going to start thank you everybody for making the session I really appreciate you sticking around this long and choosing this session another one next door my name is Rima yontel I'm a Chief Architect responsible for Telco vertical at redhead and yeah thank you very much my name is atanasatanasov I'm senior Cloud native software engineer at Tinto thank you all right and today we are going to talk about power optimization you probably have noticed that sustainability is becoming a Hot Topic and power optimization is one of the aspects of sustainability and it has two advantage over some other topics that fall under the umbrella of ESG which is environmental social and governance it's quantifiable and it can potentially save you money as my power company tells me every month when it sends me an email saying I haven't saved any money compared to my neighbors so we are going to address specifically node tuning optimizations in the stock we are going to talk about how profiles can be applied to the node to tune power specific settings and then we're gonna talk a little bit about how what Intel had contributed with their kubernetes power manager improves what you can do and we're also going to have a short demo all the way at the end it's going to be pre-recorded because we're not brave enough to have it live and for the power optimization for the node we are only going to talk about what you can do with capabilities that I already present in the CPU so there is some work happening to do more power Savings optimizations in a wider context so for outside of the node for the whole cluster for multi-clusters for the whole domain and when I say domain what I mean is in a context of a Telco for instance a whole ran Network radio Access Network or all of 5G core Network right but we are going to start small and build so in the on the Node we're going to talk about the capabilities that the CPU exposes to the Linux kernel and what you can do from the kubernetes layer which types of constructs you can use to configure the capabilities of the CPU to provide you power optimization so I want to start with the tune D I mentioned profiles that you can apply and tune D is a utility that provides you a framework to configure certain power optimization settings on a different Hardware right so in your node and it uses profiles that come some of the profiles come out of the box so included with the system that you can apply based on the type of workloads you're go
