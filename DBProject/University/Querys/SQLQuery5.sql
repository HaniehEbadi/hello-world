USE [University]
GO

/****** Object:  UserDefinedFunction [dbo].[fnGetCourseID]    Script Date: 11/13/2021 5:26:32 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[fnGetCourseID2]	
(
	-- Add the parameters for the function here
	@CourseID NVARCHAR(2)
)
RETURNS TABLE 
AS
RETURN 
(
	-- Add the SELECT statement with parameter references here
	SELECT *
	FROM dbo.vwCollageProfessor
	WHERE CollageID LIKE @CourseID
)
GO


