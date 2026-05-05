---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Michael McCune", "Red Hat", "Bridget Kromhout", "Microsoft"]
sched_url: https://kccncna2022.sched.com/event/1C89O/sig-cloud-provider-update-michael-mccune-red-hat-bridget-kromhout-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Cloud+Provider+Update+CNCF+KubeCon+2022
slides: []
status: parsed
---

# SIG Cloud Provider Update - Michael McCune, Red Hat & Bridget Kromhout, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Michael McCune, Red Hat, Bridget Kromhout, Microsoft
- Schedule: https://kccncna2022.sched.com/event/1C89O/sig-cloud-provider-update-michael-mccune-red-hat-bridget-kromhout-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Cloud+Provider+Update+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre SIG Cloud Provider Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/1C89O/sig-cloud-provider-update-michael-mccune-red-hat-bridget-kromhout-microsoft
- YouTube search: https://www.youtube.com/results?search_query=SIG+Cloud+Provider+Update+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ECn26N_OMp4
- YouTube title: SIG Cloud Provider 2022-05-25
- Match score: 0.724
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/sig-cloud-provider-update/ECn26N_OMp4.txt
- Transcript chars: 14898
- Keywords: provider, actually, basically, updates, little, interesting, migration, accept, wonder, actual, recently, cubelet, kubecon, domain, meeting, volume, saying, version

### Resumo baseado na transcript

hello everybody welcome to the sig cloud fighter uh meeting wednesday may 25th um we will be going ahead and getting started so we're going to go ahead and start with triage and it looks like we have three issues um [Music] some of these look a little bit familiar um amount device failed for volume it looks like they say they're using aws ebs entry dynamic provisioning down at the bottom of that section i don't know if that that is relevant certainly uh where do you see that

### Excerpt da transcript

hello everybody welcome to the sig cloud fighter uh meeting wednesday may 25th um we will be going ahead and getting started so we're going to go ahead and start with triage and it looks like we have three issues um [Music] some of these look a little bit familiar um amount device failed for volume it looks like they say they're using aws ebs entry dynamic provisioning down at the bottom of that section i don't know if that that is relevant certainly uh where do you see that uh right above the what did you expect to happen uh perfect all right um let's go ahead and accept this and i can assign myself for now this one also looks relevant to me yeah i read this one and i thought it was interesting because i wonder i'm not sure but i wonder is it possible to make some of that stuff configurable because like they're noticing that there's a bunch of traffic that they don't want in their logs or whatever but like i wonder how configurable that is i don't know if that's possible but maybe that's the sort of thing that would be valuable to make configurable that sure is chatty yeah and it's actually they're running into bandwidth issues from this or yeah i think they're they're claiming that there's reit limiting that i guess this is getting in the way of traffic they care about or something i hear a trivial optimization i am interested to see what actual negative consequences they're experiencing from this because yeah i've never heard of someone um yeah i'm just wondering what metadervis what the metadata service rate limiting um manifested still itself as you know like how do they see that it interesting oh that person says that has actually changed recently interesting i think he's just referring to the um extraction to external ccm so i think this is referring to cubelet hence the hitting the metadata endpoint um of course uh go ahead and accept it and dig in a little bit more see what the issue is and then is this the one from before i think this one has been around for a little bit i actually looked at this one just because we just um put the yeah i see uh so we just put um the uh service selector um to you know like basically this person is saying we think that this is solved and then i dug in and i saw that they um are running 1.19 so like i have no idea if they've managed to reproduce it recently yeah got it i'm not i'm not sure if we can give them any solutions if they can't test with a more recent version when you see if you dig into the specific versi
