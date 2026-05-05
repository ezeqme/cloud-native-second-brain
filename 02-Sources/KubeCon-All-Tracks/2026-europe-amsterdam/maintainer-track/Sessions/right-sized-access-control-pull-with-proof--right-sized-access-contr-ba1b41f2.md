---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Stanislav Láznička", "Microsoft", "Lucas Käldström", "Upbound"]
sched_url: https://kccnceu2026.sched.com/event/2EIaE/right-sized-access-control-pull-with-proof-stanislav-laznicka-microsoft-lucas-kaldstrom-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Right-sized+Access+Control+%26+Pull+with+Proof+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Right-sized Access Control & Pull with Proof - Stanislav Láznička, Microsoft & Lucas Käldström, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Stanislav Láznička, Microsoft, Lucas Käldström, Upbound
- Schedule: https://kccnceu2026.sched.com/event/2EIaE/right-sized-access-control-pull-with-proof-stanislav-laznicka-microsoft-lucas-kaldstrom-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Right-sized+Access+Control+%26+Pull+with+Proof+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Right-sized Access Control & Pull with Proof.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EIaE/right-sized-access-control-pull-with-proof-stanislav-laznicka-microsoft-lucas-kaldstrom-upbound
- YouTube search: https://www.youtube.com/results?search_query=Right-sized+Access+Control+%26+Pull+with+Proof+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7aRWwlU_ewE
- YouTube title: Right-sized Access Control & Pull with Proof - Stanislav Láznička & Lucas Käldström
- Match score: 0.786
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/right-sized-access-control-pull-with-proof/7aRWwlU_ewE.txt
- Transcript chars: 24993
- Keywords: actually, images, request, pulled, credentials, create, cublet, secret, authorizer, credential, present, object, account, policy, access, pulling, private, exactly

### Resumo baseado na transcript

Uh I do hope that every and each of you uh read the abstract because if you didn't well we are just two silly men in funny hats. >> My name is Stlaznichka and this is my dear colleague >> Lucas Chastra >> and today we will be uh taking you on a deep dive through some of the uh enhancements that we are working on in Sig O. So uh there is a solution or was a solution uh to this problem and that is uh the always pull images uh admission controller. Uh another problem is this kind of puts your workloads in danger uh if your egress or the remote registries uh are not stable enough, right? Um and uh this kind of like I said is relevant to the uh the topic of pre-loaded images because uh there's this use case in in Kubernetes where the users are are allowed to load the images onto the node outside of of uh uh we've got uh Kubernetes service accounts which means that this this particular image was pulled by uh by using the service account credentials with with a service account of this UID name space and name.

### Excerpt da transcript

And we are off. Hello everybody. Uh I do hope that every and each of you uh read the abstract because if you didn't well we are just two silly men in funny hats. >> Yes. >> My name is Stlaznichka and this is my dear colleague >> Lucas Chastra >> and today we will be uh taking you on a deep dive through some of the uh enhancements that we are working on in Sig O. Yeah, it's uh well, you made it to the last slot of the the day, so congratulations and hopefully you're not asleep by the end of the presentation. >> We're trying to make you not not suffer too much. Uh all right. So, traditionally, uh these talks went, you know, uh through all the caps that the group was working on and we would uh speak about like each of the topics a little bit. Uh this time we're making uh something a little bit different. So here you can see that the group was not actually selecting but then there was a lot of work happening. Um and so what we're doing this time is we're going to go on a deep dive to through two of the features that we worked on.

Um so let's jump right into it. Uh changes to image pulling. So uh this is something that my colleague Anisha Shaker and me were working on. Uh and this all started in cube 132 when we decided that it would be nice uh to kind of improve uh the experience or the authentication experience um of pulling images. Right? Up until this point you if you wanted to pull a private image you pretty much had only several options. Uh you could either use the image pool secrets which is not exactly flexible like you know synchronizing your secrets all around the um all around the cluster or you could use the uh credential providers which also weren't very flexible in in any way or you would just have to rely on the clusterwide uh credentials right and so this is how the service account tokens for cube blood credential providers was born uh we basically wanted to take the FML tokens that that service account service accounts now have. And uh we we will be we wanted to find a way how the cube uh could use these and send them to credential providers so that these can then do whatever they want with them, right?

And so that's exactly what happened, right? So so the cublet is now able to request an audience scoped uh scoped token service account token and send it to a credential provider. The credential provider can then do whatever it wants. It can either send it back and that means that the image pool will be happening exactly with the service accoun
