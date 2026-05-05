---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Maksym Pavlenko", "Apple", "Samuel Karp", "Google"]
sched_url: https://kccnceu2023.sched.com/event/1HyUG/containerd-project-update-and-deep-dive-maksym-pavlenko-apple-samuel-karp-google
youtube_search_url: https://www.youtube.com/results?search_query=Containerd%3A+Project+Update+and+Deep+Dive+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Containerd: Project Update and Deep Dive - Maksym Pavlenko, Apple & Samuel Karp, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Maksym Pavlenko, Apple, Samuel Karp, Google
- Schedule: https://kccnceu2023.sched.com/event/1HyUG/containerd-project-update-and-deep-dive-maksym-pavlenko-apple-samuel-karp-google
- Busca YouTube: https://www.youtube.com/results?search_query=Containerd%3A+Project+Update+and+Deep+Dive+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Containerd: Project Update and Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyUG/containerd-project-update-and-deep-dive-maksym-pavlenko-apple-samuel-karp-google
- YouTube search: https://www.youtube.com/results?search_query=Containerd%3A+Project+Update+and+Deep+Dive+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=USmJ33jG0F4
- YouTube title: containerd: Project Update and Deep Dive - Derek McGowan, Apple
- Match score: 0.876
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/containerd-project-update-and-deep-dive/USmJ33jG0F4.txt
- Transcript chars: 18791
- Keywords: container, actually, client, transfer, little, everything, trying, process, pretty, implementation, releases, support, sandbox, containers, actual, metadata, delete, around

### Resumo baseado na transcript

all right oh welcome everybody i realized we're in like the first slot here which is it's kind of interesting so yeah it's good i'm excited to get started so as i said yeah phil's not going to be here today he's in valencia but he can't be here today unfortunately he might be on the on the virtual platform somewhere so hi phil um so today we're going to kind of give an introduction to container d go through its architecture and it's kind of where the project has

### Excerpt da transcript

all right oh welcome everybody i realized we're in like the first slot here which is it's kind of interesting so yeah it's good i'm excited to get started so as i said yeah phil's not going to be here today he's in valencia but he can't be here today unfortunately he might be on the on the virtual platform somewhere so hi phil um so today we're going to kind of give an introduction to container d go through its architecture and it's kind of where the project has been in the last year or since the last last kubecon so if there's other container detox at kubecon so i i recommend you know like the first one we have from akihiro another containery uh maintainer should be really interesting um and anusha also has a talk that's going to be covering container d as well both of those tomorrow so i'm going to start off with kind of where container d has been in the last year we've we've seen kind of tremendous growth in the project a lot of that is going to be seen from kubernetes uh 1.24 we've we finally saw the the deprecation and removal of the docker shim which has brought a lot of people thank you is that dims right there yeah yeah a lot of yeah you can thank dims for that he's worked hard on that but that is that's really driven a lot of people to container d and luckily like what we've seen is even though the number of users has gone way up the project itself hasn't seen a lot of issues people seem to have had a pretty good experience moving to container d so if you already i'm sure you're you're thinking about it uh as uh it's well you have to at some point really um and then as well as is nerd cuddle so i don't know how many of you are using nerd gotta today it's it's a pretty new tool developed by originally by aki hero we're seeing a lot of uptick in that in usage it's driving a lot of users to container d and it's really it's it's a pretty amazing project uh you should you should check it out if you haven't already um we've also have some new maintainers that have joined since last kubecon so we have kazuo as our new committer and then we also added mike and danny as reviewers one thing about our project where we're at we could always use documentation improvements especially as we have a lot of users coming in this is a great opportunity for those who want to contribute and you're not quite sure how to contribute it's understandable that contributing to a case like container d is kind of hard to get started but you know each of you are going through yo
