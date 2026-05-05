---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Networking"
themes: ["Networking"]
speakers: ["Bridget Kromhout", "Microsoft", "Tim Hockin", "Google", "Dinesh Majrekar", "Civo", "Lachie Evenson", "Microsoft", "Rags Srinivas", "InfoQ"]
sched_url: https://kccnceu2022.sched.com/event/ytt0/to-ipv6-the-dual-stack-adoption-advisory-panel-bridget-kromhout-microsoft-tim-hockin-google-dinesh-majrekar-civo-lachie-evenson-microsoft-rags-srinivas-infoq
youtube_search_url: https://www.youtube.com/results?search_query=To+IPv6+-+The+Dual-stack+Adoption+Advisory+Panel+CNCF+KubeCon+2022
slides: []
status: parsed
---

# To IPv6 - The Dual-stack Adoption Advisory Panel - Bridget Kromhout, Microsoft; Tim Hockin, Google; Dinesh Majrekar, Civo; Lachie Evenson, Microsoft; Rags Srinivas, InfoQ

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Networking]]
- Temas: [[Networking]]
- País/cidade: Spain / Valencia
- Speakers: Bridget Kromhout, Microsoft, Tim Hockin, Google, Dinesh Majrekar, Civo, Lachie Evenson, Microsoft, Rags Srinivas, InfoQ
- Schedule: https://kccnceu2022.sched.com/event/ytt0/to-ipv6-the-dual-stack-adoption-advisory-panel-bridget-kromhout-microsoft-tim-hockin-google-dinesh-majrekar-civo-lachie-evenson-microsoft-rags-srinivas-infoq
- Busca YouTube: https://www.youtube.com/results?search_query=To+IPv6+-+The+Dual-stack+Adoption+Advisory+Panel+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre To IPv6 - The Dual-stack Adoption Advisory Panel.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytt0/to-ipv6-the-dual-stack-adoption-advisory-panel-bridget-kromhout-microsoft-tim-hockin-google-dinesh-majrekar-civo-lachie-evenson-microsoft-rags-srinivas-infoq
- YouTube search: https://www.youtube.com/results?search_query=To+IPv6+-+The+Dual-stack+Adoption+Advisory+Panel+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CqfEwzXI5W0
- YouTube title: To IPv6 - The Dual-stack Adoption Advisory Panel
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/to-ipv6-the-dual-stack-adoption-advisory-panel/CqfEwzXI5W0.txt
- Transcript chars: 30062
- Keywords: actually, network, cluster, internet, question, questions, having, addressing, address, getting, provider, answer, everything, networking, little, coming, virtual, developer

### Resumo baseado na transcript

all right all right can everyone hear me perfect so those of you in the back there is a lot of room in the front you know if you want to come front you know you don't like a particular answer by one of the panelists you can even accost them you know i'm just kidding um but uh thank you for coming you know it's always a pleasure to be in person i did a lot of kubecon talks virtual right we got a what three o'clock in the have any question but you know while you're warming up uh i think that was a good segue into the question that i was gonna ask which is uh i'm a developer i'm an app developer right and uh you know kubernetes networking was great the challenges that you're going to face in service discovery and a whole bunch of other things so i think getting that end to end connectivity because we come from the ipv4 world and we all grew up under it we think we can bring

### Excerpt da transcript

all right all right can everyone hear me perfect so those of you in the back there is a lot of room in the front you know if you want to come front you know you don't like a particular answer by one of the panelists you can even accost them you know i'm just kidding um but uh thank you for coming you know it's always a pleasure to be in person i did a lot of kubecon talks virtual right we got a what three o'clock in the morning for one of these but uh but um you know it's it's great to be in person it's four o'clock it's a reasonable time people are here but this is your panel you know so be ready with the questions i'm just going to do a quick round of introductions and after that it's all yours okay so feel free to ask some of the tough questions make this panelist squirm they know everything about networking and ipv6 so you know so i think it'll be cool yeah i see that nobody knows everything about it right um before i get started how many of you are already familiar with dual stack networking okay all right how many of you are already on the ipv6 bandwagon when it comes to kubernetes whoa okay that's very cool last question on a scale of 1 to 10 a networking geek right is 10 and really know nothing about you know kind of the different levels or whatever right that's one and i'm somewhere like a level two level three something like that how many are you above a level six a level seven a few okay so you guys can't ask any questions okay no they're going to answer the questions yes no but but thanks again for coming uh this is your panel uh so um i have a great august panel in may um so it's pretty cool um i'll let them introduce themselves so be ready to ask some questions i'm gonna run around with a handheld mic please wait okay don't yell yell out because you know there are virtual audience who are listening as we speak so i don't want to ignore any of them so thanks for coming virtual audience as well uh with that said let's go from left to right or right to left or whatever they you know start with tim hi everyone my name is tim um i work at google i've been on kubernetes for a long time i'm one of the sig leads for sig networking and if you hate the dual stack api it's probably my fault i am dinesh from sivo i've been implementing some of the v6 dual stack into our cloud platform which we then offer out to customers as a kubernetes service wonderful hello everybody how's everybody doing good thank you thank you i need the energy i need the energy my
