---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Application + Development"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Aaron Alpar", "Kasten"]
sched_url: https://kccnceu2022.sched.com/event/ytlG/seeing-is-believing-debugging-with-ephemeral-containers-aaron-alpar-kasten
youtube_search_url: https://www.youtube.com/results?search_query=Seeing+is+Believing%3A+Debugging+with+Ephemeral+Containers+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Seeing is Believing: Debugging with Ephemeral Containers - Aaron Alpar, Kasten

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Application + Development]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: Spain / Valencia
- Speakers: Aaron Alpar, Kasten
- Schedule: https://kccnceu2022.sched.com/event/ytlG/seeing-is-believing-debugging-with-ephemeral-containers-aaron-alpar-kasten
- Busca YouTube: https://www.youtube.com/results?search_query=Seeing+is+Believing%3A+Debugging+with+Ephemeral+Containers+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Seeing is Believing: Debugging with Ephemeral Containers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytlG/seeing-is-believing-debugging-with-ephemeral-containers-aaron-alpar-kasten
- YouTube search: https://www.youtube.com/results?search_query=Seeing+is+Believing%3A+Debugging+with+Ephemeral+Containers+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=obasTgzhVR0
- YouTube title: Seeing is Believing: Debugging with Ephemeral Containers - Aaron Alpar, Kasten
- Match score: 0.933
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/seeing-is-believing-debugging-with-ephemeral-containers/obasTgzhVR0.txt
- Transcript chars: 31599
- Keywords: container, containers, ephemeral, spaces, debugging, little, access, command, basically, target, running, postgres, network, presentation, process, important, default, emeral

### Resumo baseado na transcript

hello welcome hey my name is Linda I'm the moderator for this session I work for a small company solo.io we specialize in application networking we still have some spaces up front if you are brave enough to walk on the first row second row so um please welcome Aon to um present you our scene is believing debugging with feral containers okay thank [Applause] you okay let's get going here uh so um see if I can make this work up a little ahead of getting a little ahead

### Excerpt da transcript

hello welcome hey my name is Linda I'm the moderator for this session I work for a small company solo.io we specialize in application networking we still have some spaces up front if you are brave enough to walk on the first row second row so um please welcome Aon to um present you our scene is believing debugging with feral containers okay thank [Applause] you okay let's get going here uh so um see if I can make this work up a little ahead of getting a little ahead of myself here there we go make sure uh PowerPoint is going to do what I need to do okay so I'm going to be talking about uh ephemeral containers uh today of course uh I'm Aaron alpar uh I work with Casten uh software engineer with Casten uh I do software engineer sort of stuff I I primarily focus on the uh uh the data layer persistence um so uh today I'm going to talk about uh ephemeral containers so and what's important about ephemeral containers is that the they are more than just containers that stick around for just a little while they are uh a very important piece to uh kubernetes architecture uh I'm going to give you a little bit of that and uh hopefully uh reasons why as well as a lot of the technical background that makes ephemeral containers work and hopefully by seeing that technical background uh you'll get an understanding of what their power is um so anyhow uh so let me proceed uh this is going to be a pretty technical presentation so I I encourage you to download the slides uh that are up on skedge for this uh I just happen to update them about a half an hour ago so if you've already downloaded them try to download them again the content remains largely the same so the ordering of a few of the slides and I've emphasized some details in the new ones so if you're following along I encourage you definitely encourage you to download the slides uh I've got a lot of console type text in here a couple of slides uh the fonts are small so I'm hoping that uh folks can see them yet another reason uh to download the presentation uh anyhow let me get started um before I get started about talking about ephemeral containers I'm could to talk about what you what you're going to need in this presentation this presentation is a uh is uh both me presenting and talking about it uh as well as a sort of self-driven tutorial so so I'll talk about that as we go along uh to make this to make this tutorial work uh you're going to need uh and this this is designed to do after the presentation uh I don't tr
