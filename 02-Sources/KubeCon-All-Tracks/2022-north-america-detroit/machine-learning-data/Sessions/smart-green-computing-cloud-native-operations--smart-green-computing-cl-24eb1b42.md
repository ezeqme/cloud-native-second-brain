---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "Sustainability"]
speakers: ["William Caban", "Federico Rossi", "Red Hat"]
sched_url: https://kccncna2022.sched.com/event/182ER/smart-green-computing-cloud-native-operations-william-caban-federico-rossi-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Smart+Green+Computing+Cloud+Native+Operations+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Smart Green Computing Cloud Native Operations - William Caban & Federico Rossi, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[Sustainability]]
- País/cidade: United States / Detroit
- Speakers: William Caban, Federico Rossi, Red Hat
- Schedule: https://kccncna2022.sched.com/event/182ER/smart-green-computing-cloud-native-operations-william-caban-federico-rossi-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Smart+Green+Computing+Cloud+Native+Operations+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Smart Green Computing Cloud Native Operations.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182ER/smart-green-computing-cloud-native-operations-william-caban-federico-rossi-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Smart+Green+Computing+Cloud+Native+Operations+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cuzj-gUfYXA
- YouTube title: Smart Green Computing Cloud Native Operations - William Caban & Federico Rossi, Red Hat
- Match score: 0.789
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/smart-green-computing-cloud-native-operations/cuzj-gUfYXA.txt
- Transcript chars: 24677
- Keywords: metrics, scheduler, policy, workload, cluster, schedule, scheduling, basically, certain, driven, metric, called, everyone, working, happened, talking, another, single

### Resumo baseado na transcript

thank you everyone for being here on a Friday very very late Friday on keep calm uh so my name is William kiban and this is uh Federico Rossi we are some typical guys working at Red Hat so why does two Telco guys are working on sustainability well it happened that the Telco itself the Telco industry represent about two percent of the total Humanity consumption of energy so yes we should be doing something and this is part of an integration work that we created and what's in node four that is not in violation of a policy so this is for CO2 but again but solution architecture that you saw and the com the components put it all together it opens a lot of possibility of the things that you can do

### Excerpt da transcript

thank you everyone for being here on a Friday very very late Friday on keep calm uh so my name is William kiban and this is uh Federico Rossi we are some typical guys working at Red Hat so why does two Telco guys are working on sustainability well it happened that the Telco itself the Telco industry represent about two percent of the total Humanity consumption of energy so yes we should be doing something and this is part of an integration work that we created and what's in the name is following so smart because we want to make sure that we can do far more than just a traditional automations we want to be able to use machine learning models and apply AI to achieve certain goals in this particular case we are talking about the goal of Green Computing and following Cloud native principles and it should work for experimentation and the same sexual work for operations so that's that's really what this means now some concept here goal-driven workload management let's start with that and the idea here is that we don't want just to go and have another specialized orchestrator we want to be able to Define goals today we're talking about for example the goal of okay let's let's do a certain amount of Maximum certain amount of CO2 on cluster upper node in material of the source that that particular node or cluster can be uh being powered by so you see there for example on carbon petroleum and the others each one of them has certain penalty on the CO2 emission but when we talk about a goal driven basically orchestration so for example the traditional way here everything will pretty much be spread across and our CO2 will be off now if I set up a goal when I go back to the goal driven workload management when we set up a goal what's going to happen is that it will really focus on achieving that even when there are compute resources available see if let's say in this case the the future workload cannot for example that has five units of penalty and there's no way even when there's compute there's no way to put that there or make it run without breaking the the goal okay so that that's part of the the idea behind the goal driven workload and the same applied to any other goal which could be like okay I want to run this on more power efficient nodes or run this to reduce my energy consumption or to have higher availability or lower latency to our customers so that's the idea here and it applies the same for node old clusters uh another concept is the idea of domain aware
