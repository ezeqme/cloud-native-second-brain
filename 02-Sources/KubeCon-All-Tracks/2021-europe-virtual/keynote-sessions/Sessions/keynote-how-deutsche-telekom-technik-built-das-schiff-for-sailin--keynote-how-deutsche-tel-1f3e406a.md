---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Keynote Sessions"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Vuk Gojnic", "Squad Lead", "Container", "Cloud-native Engine", "Deutsche Telekom Technik"]
sched_url: https://kccnceu2021.sched.com/event/iERE/keynote-how-deutsche-telekom-technik-built-das-schiff-for-sailing-the-cloud-native-seas-vuk-gojnic-squad-lead-container-cloud-native-engine-deutsche-telekom-technik
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+How+Deutsche+Telekom+Technik+Built+Das+Schiff+for+Sailing+the+Cloud+Native+Seas+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Keynote: How Deutsche Telekom Technik Built Das Schiff for Sailing the Cloud Native Seas - Vuk Gojnic, Squad Lead, Container & Cloud-native Engine, Deutsche Telekom Technik

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: Virtual / Virtual
- Speakers: Vuk Gojnic, Squad Lead, Container, Cloud-native Engine, Deutsche Telekom Technik
- Schedule: https://kccnceu2021.sched.com/event/iERE/keynote-how-deutsche-telekom-technik-built-das-schiff-for-sailing-the-cloud-native-seas-vuk-gojnic-squad-lead-container-cloud-native-engine-deutsche-telekom-technik
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+How+Deutsche+Telekom+Technik+Built+Das+Schiff+for+Sailing+the+Cloud+Native+Seas+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Keynote: How Deutsche Telekom Technik Built Das Schiff for Sailing the Cloud Native Seas.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iERE/keynote-how-deutsche-telekom-technik-built-das-schiff-for-sailing-the-cloud-native-seas-vuk-gojnic-squad-lead-container-cloud-native-engine-deutsche-telekom-technik
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+How+Deutsche+Telekom+Technik+Built+Das+Schiff+for+Sailing+the+Cloud+Native+Seas+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=s0UKWiNNFTM
- YouTube title: How Deutsche Telekom Technik Built Das Schiff for Sailing the Cloud Native Seas - Vuk Gojnic
- Match score: 0.973
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/keynote-how-deutsche-telekom-technik-built-das-schiff-for-sailing-the/s0UKWiNNFTM.txt
- Transcript chars: 7299
- Keywords: platform, native, network, locations, scenario, infrastructure, manage, cluster, working, clusters, functions, pieces, approach, deutsche, telekom, managing, hundreds, running

### Resumo baseado na transcript

[Music] do you know how does it look like to provide a managed kubernetes service in a telco it means managing hundreds even thousands of kubernetes clusters across hundreds of locations what kind of locations well this might look familiar or even this but it is also this as an industry we are not quite yet there but the speed with which we are approaching to this scenario is enormous hello everybody i am vu going each and since two years i'm running kubernetes platform team of deutsche telekom technique

### Excerpt da transcript

[Music] do you know how does it look like to provide a managed kubernetes service in a telco it means managing hundreds even thousands of kubernetes clusters across hundreds of locations what kind of locations well this might look familiar or even this but it is also this as an industry we are not quite yet there but the speed with which we are approaching to this scenario is enormous hello everybody i am vu going each and since two years i'm running kubernetes platform team of deutsche telekom technique a network technology unit of deutsche telekom in germany my cloud native journey started in mid of 2019 when i was asked to look into providing a kubernetes platform for a telco workloads what kind of workloads well it is certainly not what you are expecting in an enterprise unless if you are coming from a telco we run the service platforms and network functions uh there many of those you are using even right now to participate in the kubecon uh which is the the technology which is highly and then very fast proliferating in that space can you guess it i guess you guessed it well it is a 5g and this is also what we are building and providing our platform for because it also requires platform infrastructure to run somewhere we asked ourselves when we began how could we provision maintain and manage kubernetes clusters the kubernetes tax at that scale with a small relatively small people of not more than sres and we looked into what is uh what is common in the industry and one of the common and accepted statements is that kubernetes is mature for production as it is and this if this was the true in 2018 uh it is even more true in 2020 and it's true not only for kubernetes but for many other pieces of a cloud native technologies they are of course many advanced solutions and distributions on the market and each of those is bringing a lot of options and benefits the question is what do you need and we found just enough of what we need for our use case in cncf we got inspired by those who did the same or similar thing before us and we decided to follow their path fail we may say we must expecting long journey we gave our project symbolic name dashif which is a german for the ship and our small but growing team eagerly earmarked the pieces came together in a platform in the platform by usage of and combination of cluster api and flux cd this enabled us to enjoy all the benefits of git tops as pioneered by vworks however in this case for a managing telco and 5g in
