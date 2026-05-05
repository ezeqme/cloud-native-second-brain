---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "101 Track"
themes: ["101 Track"]
speakers: ["Adelina Simion", "Form3"]
sched_url: https://kccnceu2022.sched.com/event/ytpu/choosing-cloud-native-technologies-for-the-journey-to-multi-cloud-adelina-simion-form3
youtube_search_url: https://www.youtube.com/results?search_query=Choosing+Cloud+Native+Technologies+for+the+Journey+to+Multi-cloud+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Choosing Cloud Native Technologies for the Journey to Multi-cloud - Adelina Simion, Form3

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: Spain / Valencia
- Speakers: Adelina Simion, Form3
- Schedule: https://kccnceu2022.sched.com/event/ytpu/choosing-cloud-native-technologies-for-the-journey-to-multi-cloud-adelina-simion-form3
- Busca YouTube: https://www.youtube.com/results?search_query=Choosing+Cloud+Native+Technologies+for+the+Journey+to+Multi-cloud+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Choosing Cloud Native Technologies for the Journey to Multi-cloud.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytpu/choosing-cloud-native-technologies-for-the-journey-to-multi-cloud-adelina-simion-form3
- YouTube search: https://www.youtube.com/results?search_query=Choosing+Cloud+Native+Technologies+for+the+Journey+to+Multi-cloud+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NGuiizWUuaw
- YouTube title: Choosing Cloud Native Technologies for the Journey to Multi-cloud - Adelina Simion, Form3
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/choosing-cloud-native-technologies-for-the-journey-to-multi-cloud/NGuiizWUuaw.txt
- Transcript chars: 20998
- Keywords: multi-cloud, connect, actually, particular, psyllium, payment, clouds, decided, platform, allows, architecture, cockroach, clients, provides, choose, stream, exactly, together

### Resumo baseado na transcript

okay thanks for joining this session so our next section is about choosing cloud native technology for the journey to the multi-cloud and thanks for joining this session once again including the butcher audience as well so quick introduce to myself my name is danielle i'm cnc ambassador and then a lot of stuff in track chair and a track committee member in kubecon i'm so happy to be here to introduce now our great speaker dalina from a form 3 as technical evangelist so please welcome our next great

### Excerpt da transcript

okay thanks for joining this session so our next section is about choosing cloud native technology for the journey to the multi-cloud and thanks for joining this session once again including the butcher audience as well so quick introduce to myself my name is danielle i'm cnc ambassador and then a lot of stuff in track chair and a track committee member in kubecon i'm so happy to be here to introduce now our great speaker dalina from a form 3 as technical evangelist so please welcome our next great speaker [Applause] hello everyone hi i'm adelina and today we'll be talking about form 3's journey to multi-cloud some of the technologies that we use and exactly how they fit together it's my first time at kubecon and my first time speaking on this amazing stage so and i really appreciate that so many of you took the time to hear me so daniel already said that i'm a technology evangelist of form3 but i just wanted to to give a shout out to our amazing engineering team who have done all of the great work that i will pre that i have the honor to present to you today um all right so this talk will consist of a quick introduction of why we decided to go multi-cloud and what it actually means i'll set the background and i'll show you our previous architecture and then i will introduce each of the technologies that have made the multi-cloud transition possible and in particular it'll be kubernetes psyllium nuts and cockroach db and these are amazing cloud agnostic technologies that we'll be learning about today all right so let's begin we've got a lot a lot of ground to cover first i'd like to introduce exactly what form three does so form three sits between our customers which are financial institutions and the external payments infrastructure that power interbank transactions as you can imagine banks don't directly integrate with each other that would be a maintenance nightmare instead when they um process payments in betwee between banks they go through external payments infrastructure that um actually define the standards that we use for interbank transactions and we make our customers lives easier because we take care of all of the securing of actual payments processing and then they integrate with our apis so a lot of the decisions that we make when it comes to architecture and technologies come from some of the challenges that we face in the world of payments processing first we process a huge number a huge number of transactions so we have a large volume that
