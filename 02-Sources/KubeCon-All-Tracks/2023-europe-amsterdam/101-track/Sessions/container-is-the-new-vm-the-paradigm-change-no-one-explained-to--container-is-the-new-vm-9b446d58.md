---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "101 Track"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Marga Manterola", "Isovalent", "Rodrigo Campos Catelin", "Microsoft"]
sched_url: https://kccnceu2023.sched.com/event/1HybZ/container-is-the-new-vm-the-paradigm-change-no-one-explained-to-you-marga-manterola-isovalent-rodrigo-campos-catelin-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Container+Is+the+New+VM%3A+The+Paradigm+Change+No+One+Explained+to+You+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Container Is the New VM: The Paradigm Change No One Explained to You - Marga Manterola, Isovalent & Rodrigo Campos Catelin, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[101 Track]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Marga Manterola, Isovalent, Rodrigo Campos Catelin, Microsoft
- Schedule: https://kccnceu2023.sched.com/event/1HybZ/container-is-the-new-vm-the-paradigm-change-no-one-explained-to-you-marga-manterola-isovalent-rodrigo-campos-catelin-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Container+Is+the+New+VM%3A+The+Paradigm+Change+No+One+Explained+to+You+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Container Is the New VM: The Paradigm Change No One Explained to You.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HybZ/container-is-the-new-vm-the-paradigm-change-no-one-explained-to-you-marga-manterola-isovalent-rodrigo-campos-catelin-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Container+Is+the+New+VM%3A+The+Paradigm+Change+No+One+Explained+to+You+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-daSI6fGQFA
- YouTube title: Container Is the New VM: The Paradigm Change No One Explained...- Marga Manterola & Rodrigo Catelin
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/container-is-the-new-vm-the-paradigm-change-no-one-explained-to-you/-daSI6fGQFA.txt
- Transcript chars: 21831
- Keywords: cluster, application, containers, applications, balancer, taylor, replicas, running, container, front-end, create, another, traffic, actually, security, little, specify, network

### Resumo baseado na transcript

hi I'm Rodrigo I'm software engineer at Microsoft hi I'm Marga I'm director of engineering at ISO violent a quick show of hands from these people in the audience for which of you is the first kubecon wow all right welcome welcome everybody to kubecon and welcome also those that are veterans uh we are really glad that you are here this talk is intended for people that are still thinking of managing VMS rather than containers or perhaps you've started thinking about managing containers but you need a little

### Excerpt da transcript

hi I'm Rodrigo I'm software engineer at Microsoft hi I'm Marga I'm director of engineering at ISO violent a quick show of hands from these people in the audience for which of you is the first kubecon wow all right welcome welcome everybody to kubecon and welcome also those that are veterans uh we are really glad that you are here this talk is intended for people that are still thinking of managing VMS rather than containers or perhaps you've started thinking about managing containers but you need a little Notch to make the the shift to Cloud native in fact uh I'd like to introduce you to our friend Taylor who's a system administrator that is currently managing VMS they use infrastructure as code using terraform and ansible and it works they have an application that has a front-end a vacuum some load balancing some firewalls and as I said it mostly works but as the application becomes more complex it's getting harder for them to keep up so they have been doing some research into containers and coordinators and they have decided to migrate but they need a little help so we are here to help them make that transition so let's start at the beginning Rodrigo what makes containers so special right so containers are lightweight and very easy to migrate from one node to another because they contain all the necessary necessary code to run our applications and they are not tied to the underlying host so uh you probably shot this before but we'll go over it one more time quickly uh containers help us to treat our our applications as cattle rather than pets when we treat our applications as pets we usually for each application we create a VM image with a very specific version of Linux with I don't know Ruby 3.1 no other version all its dependencies and we treat each VM with a lot of care we spend a lot of time to upgrade them with a lot of care if something fake breaks with the Sage into them to fix it when we treat our infrast cattle like no just can come and go and if a note fails we just move the applications to another node right and this and this really well tune it's just one container that we can move to the next machine but as our employ as applications become more complex we can have a front-end service a vacuum service some database some blob storage we add load balancing we want High availability it all starts to become quite complex quite fast right that's why uh we want to automate more tasks we want that for us to be roughly the same effort to keep one re
