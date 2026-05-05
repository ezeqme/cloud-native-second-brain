---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Capture The Flag"
themes: ["Capture The Flag"]
speakers: ["Andrew Martin", "James Cleverley-Prance", "ControlPlane"]
sched_url: https://kccnceu2023.sched.com/event/1Jgxu/an-introduction-to-cloud-native-capture-the-flag-andrew-martin-james-cleverley-prance-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=An+Introduction+to+Cloud+Native+Capture+The+Flag+CNCF+KubeCon+2023
slides: []
status: parsed
---

# An Introduction to Cloud Native Capture The Flag - Andrew Martin & James Cleverley-Prance, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Capture The Flag]]
- Temas: [[Capture The Flag]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Andrew Martin, James Cleverley-Prance, ControlPlane
- Schedule: https://kccnceu2023.sched.com/event/1Jgxu/an-introduction-to-cloud-native-capture-the-flag-andrew-martin-james-cleverley-prance-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=An+Introduction+to+Cloud+Native+Capture+The+Flag+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre An Introduction to Cloud Native Capture The Flag.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Jgxu/an-introduction-to-cloud-native-capture-the-flag-andrew-martin-james-cleverley-prance-controlplane
- YouTube search: https://www.youtube.com/results?search_query=An+Introduction+to+Cloud+Native+Capture+The+Flag+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Id3FJDnont4
- YouTube title: An Introduction to Capture The Flag
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/an-introduction-to-cloud-native-capture-the-flag/Id3FJDnont4.txt
- Transcript chars: 18562
- Keywords: basically, metrics, victoria, tomorrow, access, graphana, config, cluster, scenario, endpoint, credentials, questions, running, everything, scenarios, install, around, namespace

### Resumo baseado na transcript

I work for control plane and we're running these capture the flag events at CubeCon. So in my day job I help customers like governments, financial institutions and so on to basically secure their cloud estate. All right, the rest of the session I will basically run you through um a scenario we run at CubeCon India earlier this year where we basically break into a Kubernetes cluster that is running Graphana and Victoria metrics. Once you connect via SSH, you will land inside a pot inside this vulnerable Kubernetes cluster. And once you get in there, as I said, you will land in a pot inside this vulnerable Kubernetes cluster. In this scenario, it is all about observability and metrics and everything that can go wrong when you integrate tools like Graphana and Victoria metrics.

### Excerpt da transcript

Welcome everyone to introduction to um capture the flag. Uh I'm Fabian. I work for control plane and we're running these capture the flag events at CubeCon. I don't know for several years basically forever I think. Uh we're security consultancy. So in my day job I help customers like governments, financial institutions and so on to basically secure their cloud estate. everything from containers to Kubernetes, CI/CD and so on. Um yeah, we're about 50 people across UK, um Europe, North America and APEC. And we basically run these CTFs to basically teach you about common security pitfalls. We we see out there in the wild, right? We design these vulnerable Kubernetes clusters, vulnerable on purpose, so that you can basically break into them uh and see how an attacker would approach this. this scenario. So we had one introduction session in the morning. This one is the the second one for today. And then tomorrow we have the main event, right? We run the actual capture the flag event from tomorrow 11:00 a.m.

basically throughout the whole day. And you can come here, you get credentials from us to connect to this Kubernetes cluster and then solve different challenges, right? You don't need anything on your machine except SSH and a web browser. Everything else we will provide for you. All right, as I said, there are three different scenarios for you to solve tomorrow. And these are brought to you by Andrea and Gabriella. They're the security engineers at control plane who came up with these interesting scenarios and put together the the vulnerable Kubernetes cluster. So if you want to give them a shout out uh after playing, they would appreciate it. Um yeah, what to expect. So in terms of organization um you have to connect to the CNCF slack. So if you haven't done that, do that by tomorrow and there's a CubeCon NACTF channel um where you find the control plane taskmaster and you can basically ask them that will be me uh to provide your credentials uh and then you get access you get an SSH key you get an SSH config and then you can connect um to the cluster and and start breaking it.

There will be three different sets of credentials for three different scenarios and each scenario also has three flags, right? So for a total of nine to find these flags always have the following pattern. So flag ctf and then some long string. When you find something that resembles this fleck, this is your solution, right? This is what you're looking for in this Kubernetes cluster.
