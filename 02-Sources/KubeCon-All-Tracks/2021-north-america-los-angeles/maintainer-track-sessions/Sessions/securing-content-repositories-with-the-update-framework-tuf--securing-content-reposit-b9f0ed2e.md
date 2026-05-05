---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Marina Moore", "NYU", "Joshua Lock", "VMware"]
sched_url: https://kccncna2021.sched.com/event/lV86/securing-content-repositories-with-the-update-framework-tuf-marina-moore-nyu-joshua-lock-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Securing+Content+Repositories+with+the+Update+Framework+%28TUF%29+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Securing Content Repositories with the Update Framework (TUF) - Marina Moore, NYU & Joshua Lock, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Marina Moore, NYU, Joshua Lock, VMware
- Schedule: https://kccncna2021.sched.com/event/lV86/securing-content-repositories-with-the-update-framework-tuf-marina-moore-nyu-joshua-lock-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+Content+Repositories+with+the+Update+Framework+%28TUF%29+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Securing Content Repositories with the Update Framework (TUF).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV86/securing-content-repositories-with-the-update-framework-tuf-marina-moore-nyu-joshua-lock-vmware
- YouTube search: https://www.youtube.com/results?search_query=Securing+Content+Repositories+with+the+Update+Framework+%28TUF%29+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Xuk3BcluYxw
- YouTube title: Securing Content Repositories with the Update Framework (TUF) - Marina Moore, NYU & Joshua Lock
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/securing-content-repositories-with-the-update-framework-tuf/Xuk3BcluYxw.txt
- Transcript chars: 21667
- Keywords: content, implementation, repository, specification, working, metadata, pieces, various, anything, reference, notary, package, addition, signing, systems, practice, software, signatures

### Resumo baseado na transcript

I'm a PhD student at NYU in the secure systems lab working with Justin Cappos and many others on TUF and other projects. My co-presenter, Joshua Lock, unfortunately was not able to make it here today, but I want to give him credit for help with the slides and and everything else. version that maybe has known vulnerabilities or some other problems or just show you different different versions of different packages that were never available at the same time. It's a framework for secure software updates that's designed to protect the the freshness, consistency, and integrity of packages. And so, this this has been kind of a bit of a redesign and rethink of how we want to do this whole project. Here's a quick diagram of the um, kind of the current design for this this TUF Notary work um, that involves uh, in order to allow for um, using TUF metadata across multiple different repositories on one registry or on many registries, um, this design separates out the TUF repository um, from the content itself.

### Excerpt da transcript

Say hello everyone. I'm Marina Moore. I'm a PhD student at NYU in the secure systems lab working with Justin Cappos and many others on TUF and other projects. My co-presenter, Joshua Lock, unfortunately was not able to make it here today, but I want to give him credit for help with the slides and and everything else. So, All right. So, what are we talking about today? Content repositories. So, content repository is basically just any kind of collection of content, usually somehow able to be addressed by a user. Often with various different versions of the content all stored in the same place and accessible. So, as a quick example of what one of these can look like, we have various different packages stored on the content repository with different versions of this package all associated with the name of of the package. And there's also an index, which then points to all of these different all the different content on the repository, which the user can then talk to this index to either find the name of a package that they're looking for or the you know the most recent version of a package or a specific version.

The index will then point them to a path to the the exact image they want to install, which they can then query and get onto their machine. Kind of an overall view of how that works. However, as with as with many systems, there are a lot of things that can go wrong if pieces of these of the system are attacked. So, if an attacker is able to gain access to this index, they're able to change either the location of the package that you're going to download or they're able to change the version that you're going to download and maybe show you an older version that maybe has known vulnerabilities or some other problems or just show you different different versions of different packages that were never available at the same time. And these different versions could maybe have some incompatibilities that can lead to other vulnerabilities. And then when when you request from this malicious index, it'll give you a bad path or some path that you're not expecting when you want to download this this piece of content.

Another thing that can go wrong is you can you can be redirected to a whole another place to to download the package. And that can also be a bad way to go. And in addition, the entire content repository itself can be compromised and any of these different pieces of content on this repository can be replaced with malicious versions of of these packag
