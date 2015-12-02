<#-- users -->
<h2>Users S</h2>
<#assign userStar = rest("2.0","/search?q=" + "SELECT * FROM users WHERE roles.id = 't:Nivel3_C_PE' ORDER BY login DESC LIMIT 10000"?url) />

<ul>
<#list userStar.data.items as user >
<#assign msg = rest("2.0","/search?q=" + "${user.messages.query} LIMIT 1000"?url) />
<#-- <#assign blogs = rest("2.0","/search?q=" + "${user.topics.query} LIMIT 1000"?url) /> -->
<#assign solutions = rest("2.0","/search?q=" + "${user.solutions_authored.query} LIMIT 1000"?url) />
<#-- <#assign kudoso = rest("2.0","/search?q=" + "${user.kudos_given.query} LIMIT 1000"?url) /> -->
<#assign kudosr = rest("2.0","/search?q=" + "${user.kudos_received.query} LIMIT 1000"?url) />
<#-- <#assign reviews = rest("2.0","/search?q=" + "${user.reviews.query} LIMIT 1000"?url) /> -->
<#-- new -->
<#assign currentTime = .now>
<#assign longTime = currentTime?long>
<#assign horaAntes = longTime - 1000*60*60*24*7>
<#assign horaAntesFormat = horaAntes?number_to_datetime>
<#assign diasUser = user.last_visit_time?long - horaAntes>
	<#if diasUser gt 0>
		<li>
		${user.id}-${user.login} [
    	<#assign y = 0>
	    <#list msg.data.items as m>
			<#assign diasMsg = m.post_time?long - horaAntes>
			<#if diasMsg gt 0>
				<#assign y = y+1>
				M${y}
			</#if>
		</#list>
		<#assign x = 0>
		-
    	<#list kudosr.data.items as kr>
			<#assign diasK = kr.time?long - horaAntes>
			<#if diasK gt 0>
				<#assign x = x+1>
				K${x}
			</#if>
		</#list>
		-
		<#assign z = 0>
		<#list solutions.data.items as sol>
			<#assign diasS = sol.post_time?long - horaAntes>
			<#if diasS gt 0>
				<#assign z = z+1>
				S-${z}
			</#if>
		</#list>]
    	</li>
    </#if>
</#list>
</ul>




<#if msg.data.size != 0>
    ${user.id} - ${user.login} - kr=${kudosr.data.size} - ko=${kudoso.data.size} - blogs=${blogs.data.size} - reviews=${reviews.data.size} - msj=${msg.data.size} - sol=${solutions.data.size} - ${user.last_visit_time?long} - ${dias} - ${horaAntesFormat}
</#if>

<#assign aDateTime = .now>
<#assign aDateTimeLong = aDateTime?long>
<#assign anHourAgoLong = aDateTimeLong - 3600000> 
<#assign anHourAgo = anHourAgoLong?number_to_datetime>
<#assign visits_count = restadmin("metrics/name/billing_visits?date_start=" + anHourAgo?iso_utc + "&date_end=" + aDateTime?iso_utc + "").value?number />       
<h2>${visits_count?string(",##0")}</h2>


<#-- kudos -->
<h2>Users 15</h2>
<#assign kudos = rest("2.0","/search?q=" + "SELECT * FROM kudos WHERE message.author.id = '15'"?url) />
<#if kudos.data.size != 0>
    ${user.login} - k=${kudos.data.size} - tp=${tp.data.size} - rv=${rv.data.size} - msj=${msg.data.size}
</#if>


<#-- selects  -->
SELECT * FROM users LIMIT 1

SELECT * FROM users WHERE rank.id="43" LIMIT 1

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vitae, molestias, ab minima tempora nihil natus quae laborum sint corporis esse debitis omnis nulla, praesentium dicta sit nobis deleniti. Aperiam, at.

<#-- users -->
<h2>Users S</h2>
<#assign userStar = rest("2.0","/search?q=" + "SELECT * FROM users ORDER BY login DESC LIMIT 10000"?url) />
<ul>
<#list userStar.data.items as user >
<li>
<#assign msg = rest("2.0","/search?q=" + "${user.messages.query} LIMIT 1000"?url) />
<#assign blogs = rest("2.0","/search?q=" + "${user.topics.query} LIMIT 1000"?url) />
<#assign solutions = rest("2.0","/search?q=" + "${user.solutions_authored.query} LIMIT 1000"?url) />
<#assign kudoso = rest("2.0","/search?q=" + "${user.kudos_given.query} LIMIT 1000"?url) />
<#assign kudosr = rest("2.0","/search?q=" + "${user.kudos_received.query} LIMIT 1000"?url) />
<#assign reviews = rest("2.0","/search?q=" + "${user.reviews.query} LIMIT 1000"?url) />
<#-- new -->
<#assign currentTime = .now>
<#assign longTime = currentTime?long>
<#assign horaAntes = longTime - 1000*60*60*24*7> 
<#assign horaAntesFormat = horaAntes?number_to_datetime>
<#assign dias = user.last_visit_time?long - horaAntes>
	<#if dias gt 0>
    	${user.id} - ${user.login} - kr=${kudosr.data.size} - ko=${kudoso.data.size} - blogs=${blogs.data.size} - reviews=${reviews.data.size} - msj=${msg.data.size} - sol=${solutions.data.size} - ${user.last_visit_time?datetime} - ${currentTime} - ${dias}
    </#if>
</li>
</#list>
</ul>
