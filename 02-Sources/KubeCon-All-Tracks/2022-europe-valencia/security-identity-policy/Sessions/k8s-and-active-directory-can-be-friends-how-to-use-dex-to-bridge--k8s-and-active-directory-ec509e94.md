---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Security + Identity + Policy"
themes: ["Security"]
speakers: ["Onkar Bhat", "Kasten by Veeam"]
sched_url: https://kccnceu2022.sched.com/event/ytkX/k8s-and-active-directory-can-be-friends-how-to-use-dex-to-bridge-the-gap-onkar-bhat-kasten-by-veeam
youtube_search_url: https://www.youtube.com/results?search_query=K8s+and+Active+Directory+Can+Be+Friends%21+How+to+Use+Dex+to+Bridge+the+Gap+CNCF+KubeCon+2022
slides: []
status: parsed
---

# K8s and Active Directory Can Be Friends! How to Use Dex to Bridge the Gap - Onkar Bhat, Kasten by Veeam

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: Spain / Valencia
- Speakers: Onkar Bhat, Kasten by Veeam
- Schedule: https://kccnceu2022.sched.com/event/ytkX/k8s-and-active-directory-can-be-friends-how-to-use-dex-to-bridge-the-gap-onkar-bhat-kasten-by-veeam
- Busca YouTube: https://www.youtube.com/results?search_query=K8s+and+Active+Directory+Can+Be+Friends%21+How+to+Use+Dex+to+Bridge+the+Gap+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre K8s and Active Directory Can Be Friends! How to Use Dex to Bridge the Gap.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytkX/k8s-and-active-directory-can-be-friends-how-to-use-dex-to-bridge-the-gap-onkar-bhat-kasten-by-veeam
- YouTube search: https://www.youtube.com/results?search_query=K8s+and+Active+Directory+Can+Be+Friends%21+How+to+Use+Dex+to+Bridge+the+Gap+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ax0gJPKgsdU
- YouTube title: K8s and Active Directory Can Be Friends! How to Use Dex to Bridge the Gap - Onkar Bhat
- Match score: 1.009
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/k8s-and-active-directory-can-be-friends-how-to-use-dex-to-bridge-the-g/ax0gJPKgsdU.txt
- Transcript chars: 41205
- Keywords: pacman, server, tutorial, directory, config, authentication, active, application, access, cluster, called, production, search, create, deployment, client, deploy, created

### Resumo baseado na transcript

good afternoon everyone my name is omkar bhatt i am an engineering manager at castin by veeam my focus has been in the areas of authentication role-based access control multi-cluster management for the purposes of data protection of applications in kubernetes this is through our product k10 that we've built at castin really grateful to be here in person today to be during doing this tutorial in front of all of you super grateful to the reviewers and committee that spent so much time reviewing the proposals and accepting my session that i had previously and i don't see that anymore and i'm redirected to pacman on successful login alright so we're almost there i wanted to highlight the logs that you'll see in decks that will help you understand what's happening index's back end and and to also find out if the configuration that you made index is actually doing what it's supposed to the logs will be useful for that purpose so here i have four log messages that got generated when i logged in as the production

### Excerpt da transcript

good afternoon everyone my name is omkar bhatt i am an engineering manager at castin by veeam my focus has been in the areas of authentication role-based access control multi-cluster management for the purposes of data protection of applications in kubernetes this is through our product k10 that we've built at castin really grateful to be here in person today to be during doing this tutorial in front of all of you super grateful to the reviewers and committee that spent so much time reviewing the proposals and accepting my proposal so very happy to be here i'm a first time speaker at kubecon now before i move ahead to the other slides for the tutorial today a few things i want to um highlight you'll see that there's a qr code at the bottom right corner of my intro slide so do make use of that to access the github repo that i've created for the purposes of today's tutorial it has a lot of prerequisites that you you should set up in order to go through today's tutorial so that's one there's also a url there right at the bottom which will take you to the same link the next thing i want to highlight is i will pause about three times for 10 minutes in various stages of the tutorial to help unblock you guys if you have questions and if you're stuck and lucky me i have my team from castin who's going to help the audience here as well so during the breaks i'll walk down and we'll help you if you if you're stuck somewhere so i have sylvan and matt from the product team at castin and i have tom and lee from the engineering team at castle so thank you so much guys for helping out today all right so let's go to the agenda next so today i'll talk about why you might want to attend this tutorial hopefully some of you have already seen the proposal and that's why you're here but i'll double click on that a little and then i'll talk about what are active directory and ldap we'll introduce the application that we're going to be deploying today for today's tutorial that's the application that we're going to secure i'll cover open ldap dex oauth2proxy which is another open source project we'll then go through the prerequisites again and we'll set up open ldap decks over through proxy and the application as part of the tutorial i will show a demo i will be going through the same steps just like you guys today and i'll show you a demo of what secure access to that application looks like at the end of the tutorial and then we'll do more q a so that's the agenda all right so why
