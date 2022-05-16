ALTER VIEW dbo.[vwMaleStudent]
AS
SELECT *,
(SELECT S.StudentCode FROM dbo.[tbl.Student] S WHERE S.ID=P.ID) AS StudentCode
FROM dbo.[tbl.Person] P
WHERE P.IsFemale=0 
	AND (SELECT S.StudentCode FROM dbo.[tbl.Student] S WHERE S.ID=P.ID) IS NOT NULL