---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Mads Høgstedt Danquah", "Jeppe Lund Andersen", "The LEGO Group"]
sched_url: https://kccnceu2024.sched.com/event/1YePF/keeping-the-bricks-flowing-the-lego-groups-approach-to-platform-engineering-for-manufacturing-mads-hogstedt-danquah-jeppe-lund-andersen-the-lego-group
youtube_search_url: https://www.youtube.com/results?search_query=Keeping+the+Bricks+Flowing%3A+The+LEGO+Group%27s+Approach+to+Platform+Engineering+for+Manufacturing+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Keeping the Bricks Flowing: The LEGO Group's Approach to Platform Engineering for Manufacturing - Mads Høgstedt Danquah & Jeppe Lund Andersen, The LEGO Group

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: France / Paris
- Speakers: Mads Høgstedt Danquah, Jeppe Lund Andersen, The LEGO Group
- Schedule: https://kccnceu2024.sched.com/event/1YePF/keeping-the-bricks-flowing-the-lego-groups-approach-to-platform-engineering-for-manufacturing-mads-hogstedt-danquah-jeppe-lund-andersen-the-lego-group
- Busca YouTube: https://www.youtube.com/results?search_query=Keeping+the+Bricks+Flowing%3A+The+LEGO+Group%27s+Approach+to+Platform+Engineering+for+Manufacturing+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Keeping the Bricks Flowing: The LEGO Group's Approach to Platform Engineering for Manufacturing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePF/keeping-the-bricks-flowing-the-lego-groups-approach-to-platform-engineering-for-manufacturing-mads-hogstedt-danquah-jeppe-lund-andersen-the-lego-group
- YouTube search: https://www.youtube.com/results?search_query=Keeping+the+Bricks+Flowing%3A+The+LEGO+Group%27s+Approach+to+Platform+Engineering+for+Manufacturing+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SmeekXGYuFU
- YouTube title: Keeping the Bricks Flowing: The LEGO Group's Approach to Platform Engineering for Manufacturing
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/keeping-the-bricks-flowing-the-lego-groups-approach-to-platform-engine/SmeekXGYuFU.txt
- Transcript chars: 29005
- Keywords: actually, platform, product, colleagues, manufacturing, engineering, digital, little, products, instance, locations, experience, cluster, running, important, access, developer, portal

### Resumo baseado na transcript

welcome everyone thank you for joining our session this talk is about our approach to platform engineering for manufacturing at the LEGO Group and we will just dive right into it so let's talk about Lego breaks first off quick show hands how many have ever uh build a Lego set before nice thanks yeah so the LEGO Group is a toy manufacturing company and we produce a wide range of different toys um like the ones you see here and we produce these at our factories around the world

### Excerpt da transcript

welcome everyone thank you for joining our session this talk is about our approach to platform engineering for manufacturing at the LEGO Group and we will just dive right into it so let's talk about Lego breaks first off quick show hands how many have ever uh build a Lego set before nice thanks yeah so the LEGO Group is a toy manufacturing company and we produce a wide range of different toys um like the ones you see here and we produce these at our factories around the world so what you see here is one part of the manufacturing uh these are molding machines so these are the actual machines that produce the Lego bricks and the Lego elements and when the fresh bricks come out they end up in those baskets or boxes that you see at the very end of the machines if you look at this maybe there's something that stands out to you there's not a lot of people in these pictures right so automation is a big part of the manufacturing at the LEGO Group um and it's all it dependent so software supports the manufacturing and this is a software that the digital teams at the LEGO Group are writing if we look at this case what happens next is at some point these boxes will fill up they're not magical um and we have in the lower right corner corner you can see a blue vehicle that's an automatic guided vehicle so this is a robot essentially that patrols the factory floor uh when the box is full it will come over swap out the box with a an empty one and machine continues to produce and the full box will go on to the next step in the process so this is one example where automation comes in uh for our manufacturing and this is the environment that we operate in this is where we produce software and and support our teams if we zoom out just a little bit we have these factories across the world um so we're in six locations right now uh seventh will open in the near future not all factories do all the same parts of the whole manufacturing process but what is common is that we have data centers at these uh factories and whenever we talk about Edge in this talk this is these are the locations that we refer to um so essentially this is what our talk will be about how do we do Platform engineering for a context like this um but we ready for it thank you okay so now you've seen a little bit about our factories now I'd like to talk a little bit about how we organize uh the people in the group so we are a uh a bunch of digital Builders software Engineers that are doing these Integrations t
