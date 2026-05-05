---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Adolfo García Veytia", "Carlos Panato", "Chainguard", "Sascha Grunert", "Red Hat", "Stephen Augustus", "Cisco"]
sched_url: https://kccnceu2022.sched.com/event/ytrh/releasing-kubernetes-less-often-and-more-secure-the-sig-release-update-adolfo-garcia-veytia-carlos-panato-chainguard-sascha-grunert-red-hat-stephen-augustus-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Releasing+Kubernetes+Less+Often+and+More+Secure+%E2%80%93+The+SIG+Release+Update+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Releasing Kubernetes Less Often and More Secure – The SIG Release Update - Adolfo García Veytia & Carlos Panato, Chainguard; Sascha Grunert, Red Hat; Stephen Augustus, Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Adolfo García Veytia, Carlos Panato, Chainguard, Sascha Grunert, Red Hat, Stephen Augustus, Cisco
- Schedule: https://kccnceu2022.sched.com/event/ytrh/releasing-kubernetes-less-often-and-more-secure-the-sig-release-update-adolfo-garcia-veytia-carlos-panato-chainguard-sascha-grunert-red-hat-stephen-augustus-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Releasing+Kubernetes+Less+Often+and+More+Secure+%E2%80%93+The+SIG+Release+Update+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Releasing Kubernetes Less Often and More Secure – The SIG Release Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytrh/releasing-kubernetes-less-often-and-more-secure-the-sig-release-update-adolfo-garcia-veytia-carlos-panato-chainguard-sascha-grunert-red-hat-stephen-augustus-cisco
- YouTube search: https://www.youtube.com/results?search_query=Releasing+Kubernetes+Less+Often+and+More+Secure+%E2%80%93+The+SIG+Release+Update+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qhQYu077zZU
- YouTube title: Releasing Kubernetes Less Often and More Secure – The SIG Release Update
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/releasing-kubernetes-less-often-and-more-secure-the-sig-release-update/qhQYu077zZU.txt
- Transcript chars: 14501
- Keywords: release, branch, signing, started, images, working, process, secure, tooling, everybody, little, everything, survey, releases, forward, results, engineer, cherry

### Resumo baseado na transcript

hello everyone let's get started my name is carlos vanato i work for chainwalk and in kubernetes i work for a single release singular release is the sig that takes care about the release of kubernetes and all the tooling around the release engineering like for taking care of the images promotions and all the tools that makes everybody use this kubernetes my name is carlos and i'm gonna request to my colleague my name is garcia and i am also a software engineer with chain guard we originally had the included name working group we are working like to make all the everything more inclusive and one of the forces is changing the branch names across the kubernetes community and we are planning we are planning to change the kk the kubernetes could unite uh like uh information because that we would like to know the companies using kubernetes downstream to see if they're gonna be impacted and then we can plan accordingly for like changing the name how the most all the infrastructure for these changes already done consumable introspective and secure each one we'd like to drill down and open in deliverables we are looking for for example we like the the they find some deliverables you want to achieve that is the salsa compliance design release effects and hence the kubernetes

### Excerpt da transcript

hello everyone let's get started my name is carlos vanato i work for chainwalk and in kubernetes i work for a single release singular release is the sig that takes care about the release of kubernetes and all the tooling around the release engineering like for taking care of the images promotions and all the tools that makes everybody use this kubernetes my name is carlos and i'm gonna request to my colleague my name is garcia and i am also a software engineer with chain guard we originally had two more speakers scheduled to be here with us and for traveling problems they couldn't be here so sorry you're stuck with us but we are both tech leads for seek release for the release and journeys of project and we're gonna do an update on the things we've been working on before that we have sasha just giving like a few words welcome to our talk from zeke release about releasing kubernetes less often and secure unfortunately i cannot attend that is cubecon in person but i'm absolutely sure that the build for carlos and steve will work this session on behalf of jeremy and myself i really hope you enjoy this talk and always feel free to reach out if you have any questions or comments hey folks okay uh today we're gonna like give some updates and uh talk about what we did in like in the past uh release and let's say in the past year we're gonna like take like a quick look on the uh changes we made for the release cadence in the recycle and some updates on the religion release engineer and we're gonna like uh share about the the work we are being doing like creating a road map and vision in the civil relief and like in the end some shots for the community uh last year we had like a release canvas of like a form release per year and we like we felt that is not that like it was too fast and like the release team that is formed for each cycle was like a have like a hard time like to manage everything then we decided to send a release survey to see how the community feel about like having less or more releases and uh we find out that uh like the community prefer like to have three releases a year then we like that's some justification that we can uh think about and we decided to instead of four release per year now we were running three releases per year that makes like a place more sustainable for not only for the release team but also for all the other things lasty uh we introduced the in the last cycle in the 124 the fast forward and this i'm gonna give like some expla
