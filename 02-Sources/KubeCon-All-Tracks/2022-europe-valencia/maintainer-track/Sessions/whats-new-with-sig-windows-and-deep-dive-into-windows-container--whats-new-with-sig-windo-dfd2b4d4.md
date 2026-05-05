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
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Mark Rossetti", "Brandon Smith", "Microsoft", "Jay Vyas", "VMware", "Claudiu Belu", "Cloudbase Solutions"]
sched_url: https://kccnceu2022.sched.com/event/ytnC/whats-new-with-sig-windows-and-deep-dive-into-windows-container-users-mark-rossetti-brandon-smith-microsoft-jay-vyas-vmware-claudiu-belu-cloudbase-solutions
youtube_search_url: https://www.youtube.com/results?search_query=What%27s+New+With+SIG+Windows+and+Deep+Dive+Into+Windows+Container+Users+CNCF+KubeCon+2022
slides: []
status: parsed
---

# What's New With SIG Windows and Deep Dive Into Windows Container Users - Mark Rossetti & Brandon Smith, Microsoft; Jay Vyas, VMware; Claudiu Belu, Cloudbase Solutions

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Mark Rossetti, Brandon Smith, Microsoft, Jay Vyas, VMware, Claudiu Belu, Cloudbase Solutions
- Schedule: https://kccnceu2022.sched.com/event/ytnC/whats-new-with-sig-windows-and-deep-dive-into-windows-container-users-mark-rossetti-brandon-smith-microsoft-jay-vyas-vmware-claudiu-belu-cloudbase-solutions
- Busca YouTube: https://www.youtube.com/results?search_query=What%27s+New+With+SIG+Windows+and+Deep+Dive+Into+Windows+Container+Users+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre What's New With SIG Windows and Deep Dive Into Windows Container Users.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytnC/whats-new-with-sig-windows-and-deep-dive-into-windows-container-users-mark-rossetti-brandon-smith-microsoft-jay-vyas-vmware-claudiu-belu-cloudbase-solutions
- YouTube search: https://www.youtube.com/results?search_query=What%27s+New+With+SIG+Windows+and+Deep+Dive+Into+Windows+Container+Users+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=THaDy6u-Cgk
- YouTube title: What's New With SIG Windows and Deep Dive... Mark Rossetti & Brandon Smith, Jay Vyas, Claudiu Belu
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/whats-new-with-sig-windows-and-deep-dive-into-windows-container-users/THaDy6u-Cgk.txt
- Transcript chars: 21466
- Keywords: windows, container, containers, accounts, administrator, account, access, network, within, specific, information, working, cluster, kernel, isolation, logs, please, server

### Resumo baseado na transcript

this is the kubernetes sig windows uh maintainer talk and today we're going to be giving some project updates and talk about windows container users and also some updates on cubeproxy nextgen let's introduce ourselves i will start my name is mark rossetti i am a software engineer at microsoft there's some contact information for me too and i am the co-chair of sig windows next up is brandon hi i'm brandon i'm a product manager at microsoft working on pretty much all things containers and kubernetes also have some

### Excerpt da transcript

hello everybody and welcome to cubecon and cloudnativecon europe2022. this is the kubernetes sig windows uh maintainer talk and today we're going to be giving some project updates and talk about windows container users and also some updates on cubeproxy nextgen let's introduce ourselves i will start my name is mark rossetti i am a software engineer at microsoft there's some contact information for me too and i am the co-chair of sig windows next up is brandon hi i'm brandon i'm a product manager at microsoft working on pretty much all things containers and kubernetes also have some aliases there and always feel free feel free to take time and reach out to me okay hey yeah um it's jay i work with mark and claudio on the sig window site as a lead on the sig windows project and i also do some things with sig network as well i work at vmware hello my name is claudio bello i'm from global solutions and i am working as a cloud engineer uh on kubernetes and container d and i am working together with mark rosetti and jay vias um as a sick tech lead for sick windows thank you so here's an agenda of what we're going to be covering today uh first up is some project updates we'll start with uh improvements to gmsa or group managed service accounts uh since the last maintainer series update here are some updates for gmsa first one is what we're just calling v2 but that really is just a way to use gmsa identities in containers without requiring that the host be domain joined through the use of a container credential guard plugin this makes it much easier to manage your windows nodes because you don't have to worry about joining them to the active directory domain before joining them to your kubernetes cluster we have support for this in the admission web hook that's part of the windows gmsa project linked here and support was added in version 0.3.0 we also have a reference plugin implementation available at um on github this reference plugin is using an azure key vault to store the credentials for doing the domain off on behalf or in place of the having the node be part of the active directory domain and then there's more information about how all of this works under the hood at the link provided below the other big update is we now have a helm chart used that's used to deploy the all of the gmsa work that you can find in the same windows gmsa repository please check that out if you're interested the next update is this pod os field i think we've mentioned it at one of
